# 设置控制台编码为 UTF-8 以避免乱码
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$IMAGE = "lab-website-renderer:latest"
$CONTAINER = "lab-website-renderer"
$WORKING_DIR = (Get-Location).Path

Write-Host "开始构建 Docker 镜像: $IMAGE ..." -ForegroundColor Green
# 如果你因为网络问题构建失败，可以取消下面这两行的注释，并修改为你的代理端口（由于 Docker Desktop 的特性，host.docker.internal 指向宿主机）
# $HTTP_PROXY = "http://host.docker.internal:7890"
# docker build --build-arg HTTP_PROXY=$HTTP_PROXY --build-arg HTTPS_PROXY=$HTTP_PROXY --tag $IMAGE --file .\.docker\Dockerfile .

docker build --tag $IMAGE --file .\.docker\Dockerfile .

Write-Host "停止并删除可能存在的旧容器: $CONTAINER ..." -ForegroundColor Yellow
docker stop $CONTAINER 2>$null
docker rm $CONTAINER 2>$null

Write-Host "启动容器并挂载当前目录... 挂载路径: $WORKING_DIR" -ForegroundColor Green
# 如果你需要代理，除了上一段的构建代理，在运行时（启动容器时）也可能需要传递代理来保证能拉取远程数据：
# $ENV_OPTS = "-e HTTP_PROXY=$HTTP_PROXY -e HTTPS_PROXY=$HTTP_PROXY"
# docker run $ENV_OPTS --name $CONTAINER --init --interactive --tty --publish 4000:4000 --publish 35729:35729 --volume "${WORKING_DIR}:/usr/src/app" $IMAGE

docker run --name $CONTAINER --init --interactive --tty --publish 4000:4000 --publish 35729:35729 --volume "${WORKING_DIR}:/usr/src/app" $IMAGE
