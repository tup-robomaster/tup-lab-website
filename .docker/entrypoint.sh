#!/bin/bash

set -e        # 出现错误时立即终止脚本
set -o pipefail # 管道中的任何命令失败时，整个管道的返回状态码为非零

# Use local CSL schema to avoid SSL issues
export CSL_ITEM_JSON_SCHEMA_PATH=_cite/schema/csl-data.json

echo -e "\n Listing current directory:"
ls -lh

# 生成引用
echo -e "\n Generating citations with Manubot..."
if python3 _cite/cite.py; then
    echo " Citation generation completed successfully."
else
    echo " Citation generation failed. Continuing without updated references."
fi

# 启动 Jekyll 热重载服务
echo -e "\n Starting Jekyll server with livereload..."
# 移除 `&` 符号，让这个 `watchmedo` 进程在前台运行，保持容器活跃
# 移除 sed 命令，以便我们看到 Jekyll 的原始输出
watchmedo auto-restart \
    --debug-force-polling \
    --patterns="_config.yaml" \
    --signal SIGTERM \
    -- \
    bundle exec jekyll serve \
      --open-url \
      --force_polling \
      --livereload \
      --trace \
      --host=0.0.0.0

# 监听 _data 引用源变化，自动重新生成引用
# 这个命令可以继续在后台运行，因为它不是保持容器活跃的主进程
echo -e "\n Watching citation sources for changes..."
watchmedo shell-command \
    --debug-force-polling \
    --recursive \
    --wait \
    --command="python3 _cite/cite.py || echo 'Skipped citation generation due to error.'" \
    --patterns="_data/sources*;_data/orcid*;_data/pubmed*;_data/google-scholar*" &
