#!/usr/bin/env bash
#
#
find_majority_author() {
    echo -n "$1 :"
    git blame "$1" -w | perl -n -e '/^.*?\((.*?)\s+[\d]{4}/; print $1,"\n"' | sort -f | uniq -c | sort -n | tail -n 1
}

export -f find_majority_author

git ls-files -z "*.rst" | xargs -0 -I {} bash -c 'find_majority_author "{}"' _ {}
echo "Number of files per majority contributor:"
git ls-files -z "*.rst" | xargs -0 -I {} bash -c 'find_majority_author "{}"' _ {} | tr -s ' ' | cut -d ' ' -f 4- | sort | uniq -c | sort -nr
