#!/bin/bash

usage="$(basename "$0") [-h] [-p DIRECTORY] -- program to display a sorted listing of files (current directory by default) and the current date and time

where:
    -h  show help text
    -p set the directory path (default: ./)
    -r, --reverse              reverse order while sorting
    -S                         sort by file size, largest first
    -t                         sort by modification time, newest first
    -U                         do not sort; list entries in directory order
    -v                         natural sort of (version) numbers within text
    -X                         sort alphabetically by entry extension"
  
path="./"
sort=""
while getopts ':hp:UXStvr' option; do
  case "$option" in
    h) echo "$usage"
       exit
       ;;
    p) path=$OPTARG
       ;;
    U) sort=$sort$"U"
       ;;
    X) sort=$sort$"X"
       ;;
    S) sort=$sort$"S"
       ;;
    t) sort=$sort$"t"
       ;;
    v) sort=$sort$"v"
       ;;
    r) sort=$sort$"r"
       ;;
  esac
done

if [[ $sort != "" ]]; then
sort=$"-"$sort
fi
for file in $(ls $path $sort)
do
        echo $file
done

echo

date +"%d-%m-%y %T"
