---
title: Story
nav:
  order: 2
  tooltip: Read our story

---

<h2 class="story-heading"><i class="fa-brands fa-weixin" style="color: #07c160;"></i> 微信公众号文章</h2>

<div class="story-grid">
{% for article in site.data.wechat_articles %}
  {% include wechat-article-card.html
    url=article.url
    title=article.title
    cover=article.cover
    excerpt=article.excerpt
  %}
{% endfor %}
</div>

<style>
/* Headings */
.story-heading {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 3rem;
  margin-bottom: 1rem;
  font-size: 1.8rem;
  font-weight: bold;
}
.story-heading i {
  font-size: 1.9rem;
}
:root {
  --story-card-bg: #fff;
  --story-card-title-color: #222;
  --story-card-excerpt-color: #666;
  --story-card-shadow: rgba(0, 0, 0, 0.08);
  --story-card-hover-shadow: rgba(0, 0, 0, 0.12);
}

[data-dark="true"] {
  --story-card-bg: #23272e;
  --story-card-title-color: #fff;
  --story-card-excerpt-color: #ccc;
  --story-card-shadow: rgba(0, 0, 0, 0.4);
  --story-card-hover-shadow: rgba(0, 0, 0, 0.6);
}

/* Grid System */
.story-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

@keyframes cardFadeUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Base Card UI */
.story-card {
  background: var(--story-card-bg);
  border-radius: 12px;
  box-shadow: 0 4px 16px var(--story-card-shadow);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), background 0.3s;
  animation: cardFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.story-card:nth-child(1) { animation-delay: 0.1s; }
.story-card:nth-child(2) { animation-delay: 0.15s; }
.story-card:nth-child(3) { animation-delay: 0.2s; }
.story-card:nth-child(4) { animation-delay: 0.25s; }
.story-card:nth-child(5) { animation-delay: 0.3s; }
.story-card:nth-child(6) { animation-delay: 0.35s; }
.story-card:nth-child(7) { animation-delay: 0.4s; }
.story-card:nth-child(8) { animation-delay: 0.45s; }
.story-card:nth-child(n+9) { animation-delay: 0.5s; }

.story-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px var(--story-card-hover-shadow);
}

/* Shared Cover Image */
.story-card-cover {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
}

/* Title & Content Logic */
.story-card-content {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.story-card-title {
  font-size: 1.05rem;
  font-weight: bold;
  padding: 12px 16px;
  color: var(--story-card-title-color);
  transition: color 0.2s;
}

.story-card:hover .story-card-title {
  color: var(--primary, #007bff);
}

.story-card-excerpt {
  padding: 0 16px 16px 16px;
  color: var(--story-card-excerpt-color);
  font-size: 0.95rem;
  flex: 1;
}

@media (max-width: 700px) {
  .story-grid {
    gap: 16px;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  }
}
</style>

{% include section.html %}


<h2 class="story-heading"><i class="fa-brands fa-bilibili" style="color: #00a1d6;"></i> B站宣传号</h2>
{% include bilibili_carousel_tup.html %}


<h2 class="story-heading"><i class="fa-brands fa-tiktok" style="color: var(--story-card-title-color);"></i> 抖音平台</h2>

<div class="story-grid">
  <a class="story-card" href="https://www.douyin.com/user/MS4wLjABAAAAo_qudO_LybuuiO1wSKpyqCSetOIM7fNmtJvshhQknIcnqyw7ccCWMQCLMLorobKb" target="_blank">
    <div class="story-card-cover" style="background:#1a1a1a; display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden;">
      <i class="fa-brands fa-tiktok" style="font-size:4rem; color:#fff; text-shadow: 2px 2px 0 #24ffcc, -2px -2px 0 #ff0050; position:relative; z-index:2;"></i>
    </div>
    <div class="story-card-content">
      <div class="story-card-title">访问 TUP战队 抖音主页</div>
      <div class="story-card-excerpt">关注我们的抖音号，获取最新日常动向与精彩短视频片段！</div>
    </div>
  </a>
</div>