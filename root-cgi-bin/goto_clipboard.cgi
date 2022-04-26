#!/bin/bash
#Searches the content of clipboard with duckduckgo 
#"non url string/nothing" an blank page is shown.

CLIP=$(xsel -ob)
NEW_STRING=""
for c in $CLIP
do
    echo $c
    NEW_STRING+="${c}+"
done

NEW_STRING=${NEW_STRING:0:-2}

printf "%s\r\n" "W3m-control: GOTO https://duckduckgo.com/?q=${NEW_STRING}";
#delete the buffer (element in history) created between the current page and 
#the searched page by calling this script.
printf "W3m-control: DELETE_PREVBUF\r\n"
