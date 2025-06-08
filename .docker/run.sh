#!/bin/bash

# 设置代理（可选）
export HOST_IP=$(ip route | grep default | awk '{print $3}')
export HTTP_PROXY="http://$HOST_IP:7890"
export HTTPS_PROXY="http://$HOST_IP:7890"

# 镜像和容器名字
IMAGE=lab-website-renderer:latest
CONTAINER=lab-website-renderer

# 当前工作目录
WORKING_DIR=$(pwd)

# 兼容 Windows Git Bash 等
DOCKER_RUN="docker run"
if [[ $OSTYPE == msys* ]] || [[ $OSTYPE == cygwin* ]]; then
    DOCKER_RUN="winpty docker run"
    WORKING_DIR=$(cmd //c cd)
fi

# 构建镜像（可选：加 --no-cache 强制重建）
docker build \
    --build-arg HTTP_PROXY=$HTTP_PROXY \
    --build-arg HTTPS_PROXY=$HTTPS_PROXY \
    --tag $IMAGE \
    --file ./.docker/Dockerfile .

# 停止并删除旧容器（如果存在）
docker stop $CONTAINER 2>/dev/null
docker rm $CONTAINER 2>/dev/null

# 启动容器，挂载本地目录以便更新立即生效
$DOCKER_RUN \
    --name $CONTAINER \
    --init \
    --interactive \
    --tty \
    --publish 4000:4000 \
    --publish 35729:35729 \
    --volume "${WORKING_DIR}:/usr/src/app" \
    $IMAGE "$@"
