---
title: Gallery
nav:
  order: 3
  tooltip: Team album
---

# {% include icon.html icon="fa-solid fa-users" %}GALLERY

## TUP10周年特别回忆篇



## 2025 年
### 2025 超级对抗赛 中部赛区
{% assign rmuc_2025_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2025RMUC'" %}
{% assign rmuc_2025_paths = rmuc_2025_pics | map: "path" %}
{% include photo_grid.html photos=rmuc_2025_paths album_dir="gallery/pictures/2025RMUC" %}  
<!-- 参数合并到同一行 -->

### 2025 高校联盟赛 辽宁站
{% assign rmul_2025_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2025RMUL'" %}
{% assign rmul_2025_paths = rmul_2025_pics | map: "path" %}
{% include photo_grid.html photos=rmul_2025_paths album_dir="gallery/pictures/2025RMUL" %}  
<!-- 参数合并到同一行 -->

## 2024 年
### 2024 超级对抗赛 中部赛区
{% assign rmuc_2024_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2024RMUC'" %}
{% assign rmuc_2024_paths = rmuc_2024_pics | map: "path" %}
{% include photo_grid.html photos=rmuc_2024_paths album_dir="gallery/pictures/2024RMUC" %} 
 <!-- 参数合并到同一行 -->

### 2024 高校联盟赛 辽宁站
{% assign rmul_2024_pics = site.static_files | where_exp:"file", "file.path contains 'gallery/pictures/2024RMUL'" %}
{% assign rmul_2024_paths = rmul_2024_pics | map: "path" %}
{% include photo_grid.html photos=rmul_2024_paths album_dir="gallery/pictures/2024RMUL" %} 
 <!-- 参数合并到同一行 -->