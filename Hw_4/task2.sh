#!/bin/bash

grep -l "sample" * | xargs -I {} sh -c 'echo "$(grep -o "CSC510" {} | wc -l) $(stat -c%s {}) $(basename {})"' | gawk '$1 >= 3 {print $1, $2, $3}' | sed 's/file_/filtered_/g' | sort -k1,1nr -k2,2n
