#!/usr/bin/env bash
#
#
find_contributions() {
    echo "================================================== $1 ======================================================="
    git log --follow --reverse --shortstat --pretty=format:"%an (%s)" -- "$1"
}

export -f find_contributions

git ls-files -z "*.rst" | xargs -0 -I {} bash -c 'find_contributions "{}"' _ {}
