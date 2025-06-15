---
title: Projects
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}PROJECTS

正在开发中...

{% include section.html %}

## 微信公众号文章

<div class="wechat-articles-list">
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
:root {
  --card-bg: #fff;
  --card-title-color: #222;
  --card-excerpt-color: #666;
}

[data-dark="true"] {
  --card-bg: #23272e;
  --card-title-color: #fff;
  --card-excerpt-color: #ccc;
}

.wechat-articles-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 32px;
  margin: 32px 0;
}

.wechat-article-card {
  background: var(--card-bg);
  border-radius: 10px;
  box-shadow: 0 2px 12px var(--overlay);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: background 0.3s;
}

.wechat-article-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.wechat-article-cover {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.wechat-article-title {
  font-size: 1.1em;
  font-weight: bold;
  padding: 12px 16px 0 16px;
  color: var(--card-title-color);
  transition: color 0.2s;
}

.wechat-article-link:hover .wechat-article-title {
  color: var(--primary);
}

.wechat-article-excerpt {
  padding: 8px 16px 16px 16px;
  color: var(--card-excerpt-color);
  font-size: 0.98em;
  flex: 1;
}

@media (max-width: 700px) {
  .wechat-articles-list {
    gap: 20px;
  }
  .wechat-article-cover {
    height: 160px;
  }
}
</style>

{% include section.html %}



