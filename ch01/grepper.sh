#!/bin/bash
for line in `cat | python gen_regexs.py`; do
    egrep "^$line$" /usr/share/dict/words
done
exit 0
