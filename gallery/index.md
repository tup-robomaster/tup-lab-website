---
title: Gallery
nav:
  order: 4
  tooltip: Team album
---

# {% include icon.html icon="fa-solid fa-users" %}GALLERY

{% include gallery_nav.html %}

<h2 id="special">TUP10周年特别回忆篇</h2>
### 老照片
{% assign sense_2015_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2015SENSE'" %}
{% assign sense_2015_paths = sense_2015_pics | map: "path" %}
{% include photo_grid.html photos=sense_2015_paths album_dir="gallery/pictures/2015SENSE" %}  


<h2 id="year-2025">2025 年</h2>
<h3 id="2025rmuc">2025 超级对抗赛 中部赛区</h3>
{% assign rmuc_2025_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2025RMUC'" %}
{% assign rmuc_2025_paths = rmuc_2025_pics | map: "path" %}
{% include photo_grid.html photos=rmuc_2025_paths album_dir="gallery/pictures/2025RMUC" %}  
<!-- 参数合并到同一行 -->

<h3 id="2025rmul">2025 高校联盟赛 辽宁站</h3>
{% assign rmul_2025_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2025RMUL'" %}
{% assign rmul_2025_paths = rmul_2025_pics | map: "path" %}
{% include photo_grid.html photos=rmul_2025_paths album_dir="gallery/pictures/2025RMUL" %}  
<!-- 参数合并到同一行 -->

<h2 id="year-2024">2024 年</h2>
<h3 id="2024rmuc">2024 超级对抗赛 中部赛区</h3>
{% assign rmuc_2024_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2024RMUC'" %}
{% assign rmuc_2024_paths = rmuc_2024_pics | map: "path" %}
{% include photo_grid.html photos=rmuc_2024_paths album_dir="gallery/pictures/2024RMUC" %} 
{% include back-to-top.html %}

<h3 id="2024rmul">2024 高校联盟赛 辽宁站</h3>
{% assign rmul_2024_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2024RMUL'" %}
{% assign rmul_2024_paths = rmul_2024_pics | map: "path" %}
{% include photo_grid.html photos=rmul_2024_paths album_dir="gallery/pictures/2024RMUL" %} 
 <!-- 参数合并到同一行 -->
{% include back-to-top.html %}