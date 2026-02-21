#!/bin/bash

# 运行合并章节脚本
python3 scripts/merge_chapters.py

# 运行 AI 评审脚本
python3 scripts/ai_review.py

# 脚本已经包含了 git add，但确保脚本成功运行
if [ $? -ne 0 ]; then
  echo "合并章节失败，提交已取消。"
  exit 1
fi
