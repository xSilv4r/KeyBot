#!/bin/bash
hwa=$(cat $1 | awk '{print $3":"$9}' | tr --delete , |sort -t' ' -n -k2 |awk '{gsub(",","",$1);print $1" "$2" "}'|awk '{gsub(":"," ",$1);print $1$2" "}'|awk '{if(NR!=1){a[$1]=$2","a[$1]}else print $0} END{n = asorti(a, b);for (n in b) {print b[n]": ["a[b[n]]"],"}}' |awk NR\>1 | sed "1s/.*/{/") ; out=("$hwa""}");echo $out
