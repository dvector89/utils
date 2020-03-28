#!/usr/bin/env bash
set -euo pipefail 
# e: command fails
# u: undefined var
# o pipefail: pipeline fails 

# ---------------------
# Author: $AUTHOR
# Date: $DATE
# Desc: 
# ---------------------


# $0: 当前 bash 文件 
# $#: 传递给脚本的参数个数(不包括 $0 )
# $?: 上个命令的退出状态(0 表示正常退出)
# $$: 当前 bash 运行的进程 ID
# "$@": list of 传递给脚本的参数

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
