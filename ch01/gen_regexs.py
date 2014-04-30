import sys


def get_regex(word):
   regexs = []
   for i in range(0, len(word)-2):
     for j in range(i+3, len(word)+1):
       regexs.append(word[i:j])
   return regexs


def make_regex(word):
    return "(%s)" % ("|".join(get_regex(word)))


if __name__ == "__main__":
    for word in sys.stdin:
        print make_regex(word.strip())
