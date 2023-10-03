#!/bin/bash

for f in "$@"; do
    if [[ "$f" == *.txt ]]; then
        echo "Skipping $f (already ends in .txt)"
    else
        new="${f}.txt"
        c=1
        while [[ -e "$new" ]]; do
            new="${f}_$c.txt"
            c=$((c + 1))
        done
        cp "$f" "$new"
        echo "Created $new with the same contents as $f"
    fi
done