#!/bin/bash

grep -l "sample" file* | xargs -I {} bash -c 'count=$(grep -o "CSC510" {} | wc -l); grep -q -E "^([3-9]|([1-9]+[0-9]))$" <<< "$count" && echo "$count $(stat -c%s {}) {}"' | sort -k1,1nr -k2,2nr | gawk '{print $3}' | sed 's/file_/filtered_/'
