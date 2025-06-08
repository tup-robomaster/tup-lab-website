---
---
<!-- 主界面在这里修改 -->
# Welcome to TUP Robotics Lab

**TUP战队**依托于创新创业学院SH智能机器人俱乐部，由吕荣鑫老师带队指导，战队成立于2015年，在校党委的正确领导下，和历届团队成员的努力下，经过10年的发展，现已成为沈航唯一的集机械设计制造、嵌入式软硬件开发与视觉识别以及团队运营的科技创新俱乐部，俱乐部成员以参加全国大学生机器人**RoboMaster**大赛为主，辐射周边各类竞赛。随着时间的推移，俱乐部形成了自己独有的培训、选拔体系及多元化考核方式。并融合在课堂内学习到的知识与技术，将这些优势汇集到一起，造就了沈航机器人在赛场上拥有强力而稳定的表现。

{%
  include button.html
  type="docs"
  text="Bilibili"
  icon="fa-brands fa-bilibili"
  link="https://space.bilibili.com/286752024"
%}
{%
  include button.html
  type="github"
  text="GitHub"
  link="https://github.com/tup-robomaster"
%}
{%
  include button.html
  type="docs"
  text="微信公众号"
  icon="fa-brands fa-weixin"
  link="https://mp.weixin.qq.com/mp/homepage?__biz=MzkwODAwMTk4NQ==&hid=1&sn=646e27086d5836bb6cbfb369cdd08799&scene=18#wechat_redirect"
%}

{% include section.html %}

## 高光时刻-Highlights

<!-- 第一行 -->
{% capture text %}

111 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/index/10.png"
  link="research"
  title="Our Research"
  text=text
%}


<!-- 第二行 -->
{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/index/1.png"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/index/cheer.png"
  link="team"
  title="Our Team"
  text=text
%}
