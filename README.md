# TUP Lab Website 🚀

[![on-push](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-push.yaml/badge.svg)](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-push.yaml)
[![on-pull-request](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-pull-request.yaml/badge.svg)](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-pull-request.yaml)
[![on-schedule](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-schedule.yaml/badge.svg)](https://github.com/tup-robomaster/tup-lab-website/actions/workflows/on-schedule.yaml)

> **冠木承鹏，任尔狂风** —— 沈阳航空航天大学 SH 智能机器人俱乐部 TUP 战队官网

Visit the live site: **[tup-robomaster.github.io/tup-lab-website](https://tup-robomaster.github.io/tup-lab-website)**

---

## 📖 简介 | Introduction

**TUP 战队** 依托于沈阳航空航天大学创新创业学院 SH 智能机器人俱乐部。战队成立于 2015 年，经过十年的发展，现已成为沈航唯一的集机械设计制造、嵌入式软硬件开发与视觉识别以及团队运营的科技创新俱乐部。

俱乐部成员主要参加 **全国大学生机器人 RoboMaster 大赛**。我们致力于培养具有工程实践能力和团队协作精神的优秀人才。

## ✨ 核心板块 | Key Features

-   🏆 **战队成果 (Projects)**: 展示历年机器人的技术积淀，包括自瞄系统、能量机关及雷达系统。
-   📖 **战队故事 (Story)**: 记录属于 TUP 的青春回忆与热爱。
-   📜 **战队历史 (History)**: 追溯自 2015 年成立以来的每一个高光时刻，包括历年成绩与核心成员。
-   📷 **战队相册 (Gallery)**: 捕捉实验室的日常与赛场的高光时刻。
-   🚀 **了解 RoboMaster**: 传播工程师文化，诠释“初心高于胜负，成长大于输赢”。
-   🤝 **加入我们 (Join)**: 期待充满激情的你加入这片热土。

---

## 🛠️ 本地开发 | Local Development

### 使用 Docker (推荐)

项目预置了 Docker 环境，可以确保在不同操作系统下环境一致。

#### Windows (PowerShell)
```powershell
.\.docker\run.ps1
```

#### Linux / macOS
```bash
bash .docker/run.sh
```
运行后，访问 `http://localhost:4000` 即可预览网站。

### 手动安装 (Jekyll)

1.  安装 [Ruby](https://www.ruby-lang.org/) 和 [Bundler](https://bundler.io/)。
2.  安装依赖: `bundle install`
3.  启动预览: `bundle exec jekyll serve`

---

## 📂 项目结构 | Repository Structure

| 目录/文件 | 说明 |
| :--- | :--- |
| `_members/` | 成员信息 (Markdown) |
| `_history/` | 战队历年沿革 (由每年的数据独立构成) |
| `_posts/` | 博客文章/动态 |
| `_data/` | 结构化数据 (项目、视频、微信文章等) |
| `_layouts/` | 页面布局模板 |
| `assets/` | 静态资源 (CSS, JS) |
| `images/` | 图片与多媒体资源 |
| `projects/` | 项目展示页面 |
| `gallery/` | 相册页面 |

---

## 📝 维护指南 | Maintenance Guide

为了确保 TUP 战队官网持续焕发活力，请参考以下指南进行日常维护。

### 1. 战队历史沿革 (History)
-   **位置**: `_history/`
-   **操作**: 每创建一个名为 `YYYY.md` 的文件（如 `2025.md`），时间轴即会自动增加一个节点。
-   **数据项**: 包含 `year` (年份), `title` (年度主题), `achievements` (获奖列表), `members` (核心队员及其详细贡献), `projects` (技术成就)。

### 2. 成员信息 (Members)
-   **位置**: `_members/`
-   **操作**: 为每位新队员创建一个 `.md` 文件。
-   **必填项**: `name` (姓名), `image` (照片路径), `role` (队内职务), `description` (简短介绍)。
-   **社交链接**: 可以在 Front Matter 中添加 `links`（如 GitHub, WeChat）显示于个人卡片。

### 3. 动态与消息 (Posts)
-   **位置**: `_posts/`
-   **操作**: 采用 Jekyll 标准博客格式 `YYYY-MM-DD-title.md`。
-   **提示**: 它可以用于发布重磅战报或技术周报。

### 4. 结构化数据维护 (Structural Data)
-   **位置**: `_data/`
-   **微信文章**: 编辑 `wechat_articles.yaml`。
-   **B站视频**: 编辑 `bilibili_videos.yaml`。
-   **战队成果 (Robots)**: 编辑 `projects.yaml`。每个项目可配置 `title`, `subtitle`, `image`, `link` 和 `description`。
-   **成员荣誉 (Citations)**: 编辑 `citations.yaml` (如有需要)。

### 5. 图片与资源 (Media)
-   **目录**: `images/`
-   **最佳实践**:
    -   **背景图**: 对应 `images/background.png`。
    -   **标志**: `images/logo.svg`。
    -   **路径引用**: 在 Markdown 中引用图片建议使用绝对路径或 `{{ 'path/to/img' | relative_url }}`。

### 6. 发布前的最后检查 (Review Checklist)
-   [ ] **预览**: 本地运行后，分别在 PC 端和移动端检查布局。
-   [ ] **模式检查**: 切换右上角的主题开关，确保在 Dark Mode 下内容可见且美观。
-   [ ] **链接验证**: 确认所有外链（微信、B站）均能正常跳转。

---

## 📜 鸣谢 | Acknowledgments

本项目基于 [Lab Website Template](https://greene-lab.gitbook.io/lab-website-template-docs) 二次开发。

---

© 2024 TUP Robotics Lab. Built with Jekyll and ❤️.
