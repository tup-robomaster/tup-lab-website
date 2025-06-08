# start with official ruby docker image as base
FROM ruby:3.1.2

# set working directory within container
WORKDIR /usr/src/app

# pull in ruby (jekyll) and python (cite process) package info
COPY Gemfile Gemfile.lock _cite/requirements.txt ./

# install ruby packages
RUN VERSION=$(grep -A 1 'BUNDLED WITH' Gemfile.lock | tail -n 1 | xargs); \
    gem install bundler --version ${VERSION} && \
    bundle _${VERSION}_ install

# install python
# RUN apt update && apt install -y python3 python3-pip

# 使用清华源替换
RUN sed -i 's|deb.debian.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list \
    && sed -i 's|security.debian.org|mirrors.tuna.tsinghua.edu.cn/debian-security|g' /etc/apt/sources.list

# 安装 Python（分步执行）
RUN apt update \
    && apt install -y --no-install-recommends \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*
# install python packages
RUN python3 -m pip install --no-cache-dir --upgrade --requirement requirements.txt

# install python package for listening for file changes
RUN pip install "watchdog[watchmedo]==3.0.0"

# ports used by jekyll
EXPOSE 4000
EXPOSE 35729

# run jekyll and cite process
COPY .docker/entrypoint.sh /var
CMD [ "/var/entrypoint.sh" ]
