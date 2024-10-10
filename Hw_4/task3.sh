#!/bin/bash
gawk -F',' '$3==2 && substr($13, 1, 1)=="S" && $7 != "" {print $0}' titanic.csv | sed 's/\<male\>/M/g; s/\<female\>/F/g' | gawk -F',' '{if ($7 != "") {sum += $7; count += 1}} END {print "Average Age: " sum/count }'
