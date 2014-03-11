# Linux Voice Competition

Details about the competition:
http://www.linuxvoice.com/competition-time/

My solution can be run by checking out this repository and running the following:
cat wordsearch.txt | bash grepper.txt

You need to have python installed to generate the regexs.

## Timings

Timed on my thinkpad machine:

    time cat wordsearch.txt | bash grepper.sh 
    hell
    hello
    binary
    nary
    sent
    this
    coffee
    scoff
    photo
    light
    sock
    socket
    bicycle
    cycle
    
    real    0m0.137s
    user    0m0.092s
    sys 0m0.024s

## How it works

These are the steps my script uses:
- load the wordsearch into a python script `gen_regexs.py`
- The python script outputs a regex for each line consisting of each possible 4 letter or more combination.
- The bash script now passes this output into egrep which greps the dictionary file (sort of backwards huh :) for complete words matching regex.)
- egrep will print out the words.
