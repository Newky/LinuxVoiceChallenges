# Linux Voice Competition

Details about the competition:
http://www.linuxvoice.com/competition-time/

My solution can be run by checking out this repository and running the following:
cat wordsearch.txt | bash grepper.txt

You need to have python installed to generate the regexs.

## Timings

Timed on my thinkpad machine:

    $ time cat wordsearch.txt | bash grepper.sh 
    ell
    hell
    hello
    bin
    binary
    nary
    hat
    his
    nth
    sent
    that
    this
    coffee
    fee
    off
    scoff
    hot
    nip
    photo
    light
    sock
    socket
    bicycle
    cycle
    icy

    real    0m0.133s
    user    0m0.084s
    sys 0m0.020s

## How it works

These are the steps my script uses:
- load the wordsearch into a python script `gen_regexs.py`
- The python script outputs a regex for each line consisting of each possible 4 letter or more combination.
- The bash script now passes this output into egrep which greps the dictionary file (sort of backwards huh :) for complete words matching regex.)
- egrep will print out the words.
