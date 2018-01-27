#! /usr/bin/env bash

cmdname=${0##*/}

helpmsg () {
    echo "Brief:"
    echo "    config git [username]"
    echo "Usage:"
    echo "    $cmdname [username]"
    echo "Try again"
    echo ""
}

# error: missing username parameter
if [ $# -lt 1 ]; then
    helpmsg
    exit 1
fi

# error: not a git repository
if ! git status 1>/dev/null 2>&1; then
    echo "error: git repository not exist"
    helpmsg
    exit 1
fi

cd $(groot)
git config --global user.name "$1"
