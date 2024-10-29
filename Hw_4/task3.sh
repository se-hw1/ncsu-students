#!/bin/bash
cat titanic.csv | grep -E "^[0-9]+,[0-9],2" | sed 's/\r//g' | grep -E ",S$" | sed 's/,male,/,M,/g' | sed 's/,female,/,F,/g' | gawk -F, '{ print $0; if ($7 !~ /^ *$/) { sum += $7; count += 1 } } END { if (count > 0) print "Average Age:", sum/count; else print "No passengers found." }'
