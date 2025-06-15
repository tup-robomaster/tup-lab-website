# start with official ruby docker image as base
FROM ruby:3.1.2

# set working directory within container
WORKDIR /usr/src/app

# === 第一阶段：复制依赖文件并安装 Ruby Gems ===
# 先复制 Gemfile 和 Gemfile.lock 用于安装 Bundler 和依赖
COPY Gemfile Gemfile.lock ./

# install ruby packages
# 使用 set -ex 确保命令失败时立即退出，并显示执行的命令
RUN set -ex; \
    # 更新 apt 缓存并安装必要的构建工具 (build-essential) 和其他常见依赖 (libffi-dev, libgmp-dev)
    apt update && \
    apt install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libgmp-dev && \
    rm -rf /var/lib/apt/lists/*; \
    \
    # 配置 Bundler 使用 Ruby China 镜像，优先于默认的 rubygems.org
    bundle config set mirror.https://rubygems.org https://gems.ruby-china.com; \
    bundle config list; \
    \
    # 安装最新版本的 Bundler，跳过文档生成以加快速度
    gem install bundler --no-document; \
    \
    # 再次检查 Bundler 版本以确保安装成功
    BUNDLER_VERSION=$(bundler --version | awk '{print $NF}'); \
    echo "Installed Bundler Version: ${BUNDLER_VERSION}"; \
    \
    # 安装 Gemfile.lock 中指定的 Gems
    # 暂时移除 --jobs 和 --retry 来简化调试，让错误信息更清晰
    bundle install; \
    echo "Ruby Gems installed successfully.";

# === 第二阶段：安装 Python 和 Python 包 ===
# 使用清华源替换 Debian apt 源
RUN sed -i 's|deb.debian.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list \
    && sed -i 's|security.debian.org|mirrors.tuna.tsinghua.edu.cn/debian-security|g' /etc/apt/sources.list

# 安装 Python（分步执行以避免单步失败）
RUN apt update \
    && apt install -y --no-install-recommends \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 复制 Python requirements.txt
COPY _cite/requirements.txt ./

# 安装 Python 包
RUN python3 -m pip install --no-cache-dir --upgrade --requirement requirements.txt

# 安装用于监听文件变化的 Python 包
RUN pip install "watchdog[watchmedo]==3.0.0"

# === 第三阶段：复制所有应用程序文件和配置入口点 ===
# 这一步将复制所有剩余的项目文件，包括 _cite/cite.py 和所有 Jekyll 站点文件
COPY . .

# Jekyll 使用的端口
EXPOSE 4000
EXPOSE 35729

# 运行 Jekyll 和 cite 进程
# entrypoint.sh 已经在之前的构建步骤中复制，现在确保其权限正确
COPY .docker/entrypoint.sh /var/
RUN apt update && apt install -y dos2unix && rm -rf /var/lib/apt/lists/*
RUN dos2unix /var/entrypoint.sh
RUN chmod +x /var/entrypoint.sh

# 调试：再次列出文件属性并打印文件内容，确认 entrypoint.sh 正确
RUN ls -l /var/entrypoint.sh
RUN cat /var/entrypoint.sh

CMD [ "/var/entrypoint.sh" ]
