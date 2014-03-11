#!/bin/bash

DICTIONARY="/usr/share/dict/words"
#DICTIONARY="test.txt"

words=""
while read input; do
    words="$words $input"
done

echo "$words"

count=0
for word in `grep '^...' $DICTIONARY`; do
    newlineremoved_word="`printf "%s" $word`"
    echo $words | grep -q "$newlineremoved_word";
    if [ $? -eq 0 ]; then
        echo `echo -n $word`
    fi
    if [ $(( count % 10000 )) == 0 ]; then
        echo "Count is $count."
    fi
    count=$(( count + 1 ));
done
