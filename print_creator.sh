#!/usr/bin/env bash
#
#
find_creator() {
    echo -n "$1: "
    git log --reverse --pretty=format:"%an" -- "$1" | head -n 1
    echo ""
}

export -f find_creator

git ls-files -z "*.rst" | xargs -0 -I {} bash -c 'find_creator "{}"' _ {}
