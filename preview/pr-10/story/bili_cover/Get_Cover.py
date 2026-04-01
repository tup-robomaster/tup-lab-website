import os
import yaml
import requests

# 配置
INPUT_YAML = "../../_data/bilibili_videos_list_tup.yaml"
OUTPUT_YAML = "../../_data/bilibili_videos_tup.yaml"
COVER_DIR = "./"

# 创建封面目录（相对路径，不要以 / 开头）
os.makedirs(COVER_DIR, exist_ok=True)

# 请求头（模仿浏览器访问 B 站）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://www.bilibili.com"
}

# 读取输入文件
with open(INPUT_YAML, "r", encoding="utf-8") as f:
    bvid_list = yaml.safe_load(f)

result = []

for item in bvid_list:
    bvid = item["bvid"]
    api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    try:
        resp = requests.get(api_url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data["code"] == 0:
            video = data["data"]
            title = video["title"]
            cover_url = video["pic"]

            # 下载封面图
            img_data = requests.get(cover_url, headers=HEADERS).content
            cover_path = os.path.join(COVER_DIR, f"{bvid}.jpg")
            with open(cover_path, "wb") as img_file:
                img_file.write(img_data)

            result.append({
                "bvid": bvid,
                "title": title,
                # "cover": f"/{COVER_DIR}/{bvid}.jpg"
            })

            print(f"[✓] 成功处理: {bvid} - {title}")
        else:
            print(f"[×] 无效 BV: {bvid}，返回 code={data['code']}")
    except Exception as e:
        print(f"[×] 请求失败: {bvid}，错误: {e}")

# 保存 YAML 输出
with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
    yaml.dump(result, f, allow_unicode=True)

print(f"\n✅ 封面下载完成，共处理 {len(result)} 个视频。")
