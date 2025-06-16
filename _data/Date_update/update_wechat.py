#!/usr/bin/env python3
"""
微信公众号文章批量抓取工具 - 防反爬增强版
功能：
1. 批量处理多个URL
2. 自动重试机制
3. 随机请求延迟
4. UserAgent轮换
5. 代理支持
6. 结果自动保存
"""

import yaml
import re
import requests
import random
import time
from bs4 import BeautifulSoup
from datetime import datetime
import os
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置区 ============================================================
CONFIG = {
    'max_retries': 3,              # 单条URL最大重试次数
    'request_delay': (1, 3),       # 请求延迟范围(秒)
    'timeout': 10,                 # 请求超时时间
    'max_workers': 3,              # 并发线程数
    'output_file': '_data/wechat_articles.yaml',  # 输出文件路径
    'proxy': None,                 # 代理设置 例如: {'http': 'http://127.0.0.1:1080'}
}

# 核心函数 ==========================================================

class WeChatScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.proxies = CONFIG['proxy']
        
    def get_random_headers(self):
        """生成随机请求头"""
        return {
            'User-Agent': self.ua.random,
            'Referer': 'https://mp.weixin.qq.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
    
    def safe_request(self, url, retry_count=0):
        """带防反爬的请求函数"""
        try:
            # 随机延迟
            time.sleep(random.uniform(*CONFIG['request_delay']))
            
            # 发送请求
            response = self.session.get(
                url,
                headers=self.get_random_headers(),
                timeout=CONFIG['timeout']
            )
            response.raise_for_status()
            
            # 检查是否触发反爬
            if "验证" in response.text:
                raise Exception("触发微信验证")
                
            return response.text
            
        except Exception as e:
            if retry_count < CONFIG['max_retries']:
                wait_time = 2 ** retry_count  # 指数退避
                print(f"请求失败 ({str(e)}), {wait_time}秒后重试...")
                time.sleep(wait_time)
                return self.safe_request(url, retry_count + 1)
            raise

    def extract_article_info(self, html, url):
        """从HTML提取文章信息"""
        def get_js_var(var_name):
            match = re.search(f'{var_name} = ["\'](.*?)["\'];', html)
            return match.group(1) if match else None

        soup = BeautifulSoup(html, 'html.parser')
        title = get_js_var('var msg_title') or soup.title.string
        excerpt = get_js_var('var msg_desc')
        cover_url = get_js_var('var msg_cdn_url') or get_js_var('var cdn_url_235_1')

        return {
            'title': self.clean_text(title),
            'url': url,
            'excerpt': self.clean_text(excerpt),
            'cover': cover_url or "",
            'date': datetime.now().strftime('%Y-%m-%d'),
            'status': 'success'
        }

    def clean_text(self, text):
        """清理文本"""
        if not text: return ""
        text = re.sub(r'[\n\r\t]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def process_url(self, url):
        """处理单个URL"""
        try:
            html = self.safe_request(url)
            return self.extract_article_info(html, url)
        except Exception as e:
            return {
                'url': url,
                'status': 'failed',
                'error': str(e)
            }

# 批量处理 =========================================================

def batch_process(urls):
    """批量处理URL列表"""
    scraper = WeChatScraper()
    results = []
    
    with ThreadPoolExecutor(max_workers=CONFIG['max_workers']) as executor:
        futures = {executor.submit(scraper.process_url, url): url for url in urls}
        
        for future in as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                if result['status'] == 'success':
                    print(f"✅ 成功处理: {url}")
                else:
                    print(f"❌ 处理失败: {url} - {result['error']}")
                results.append(result)
            except Exception as e:
                print(f"⚠️ 异常处理: {url} - {str(e)}")
                results.append({
                    'url': url,
                    'status': 'error',
                    'error': str(e)
                })
    
    return results

def update_yaml_file(new_entries):
    """更新YAML文件"""
    # 读取现有数据
    existing_data = []
    if os.path.exists(CONFIG['output_file']):
        with open(CONFIG['output_file'], 'r', encoding='utf-8') as f:
            existing_data = yaml.safe_load(f) or []
    
    # 合并数据(去重)
    url_set = {entry['url'] for entry in existing_data}
    success_count = 0
    
    for entry in new_entries:
        if entry['status'] == 'success' and entry['url'] not in url_set:
            existing_data.append(entry)
            success_count += 1
    
    # 按日期排序
    existing_data.sort(key=lambda x: x['date'], reverse=True)
    
    # 写入文件
    with open(CONFIG['output_file'], 'w', encoding='utf-8') as f:
        yaml.dump(existing_data, f, allow_unicode=True, sort_keys=False)
    
    print(f"\n处理完成: 成功 {success_count}条, 失败 {len(new_entries)-success_count}条")
    print(f"结果已保存到: {CONFIG['output_file']}")

# 主程序 ==========================================================

def main():
    print("微信公众号文章批量抓取工具")
    print("=" * 50)
    
    # 获取输入方式选择
    print("\n请选择输入方式:")
    print("1. 手动输入URL")
    print("2. 从文件读取URL列表")
    choice = input("请输入选择(1/2): ").strip()
    
    urls = []
    if choice == '1':
        print("\n请输入URL(每行一个，输入空行结束):")
        while True:
            url = input().strip()
            if not url:
                break
            if url.startswith('http'):
                urls.append(url)
            else:
                print("忽略无效URL")
    elif choice == '2':
        file_path = input("请输入文件路径: ").strip()
        try:
            with open(file_path, 'r') as f:
                urls = [line.strip() for line in f if line.strip().startswith('http')]
            print(f"从文件读取到 {len(urls)} 个URL")
        except Exception as e:
            print(f"读取文件失败: {str(e)}")
            return
    else:
        print("无效选择")
        return
    
    if not urls:
        print("没有有效的URL输入")
        return
    
    # 开始处理
    print(f"\n开始处理 {len(urls)} 个URL...")
    results = batch_process(urls)
    
    # 保存结果
    update_yaml_file(results)

if __name__ == '__main__':
    # 安装依赖: pip install fake-useragent pyyaml requests beautifulsoup4
    main()