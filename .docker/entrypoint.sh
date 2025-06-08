#!/bin/bash

set -e  # 出现错误时立即终止脚本
set -o pipefail

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
      --host=0.0.0.0 \
    | sed "s/LiveReload address.*//g;s/0.0.0.0/localhost/g" &

# 监听 _data 引用源变化，自动重新生成引用
echo -e "\n Watching citation sources for changes..."
watchmedo shell-command \
    --debug-force-polling \
    --recursive \
    --wait \
    --command="python3 _cite/cite.py || echo 'Skipped citation generation due to error.'" \
    --patterns="_data/sources*;_data/orcid*;_data/pubmed*;_data/google-scholar*"
