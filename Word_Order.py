from collections import OrderedDict
n = int(input())
distinct_words = OrderedDict()
for m in range(n):
    word = input()
    if word not in distinct_words:
        distinct_words[word] = word
    else:
        distinct_words[word] = distinct_words[word] + ' ' + word

distinct_keys = len(distinct_words.keys())
distOccurrences = ' '.join(str(len(v.split(' '))) for k,v in distinct_words.items())
print (distinct_keys)
print (distOccurrences)