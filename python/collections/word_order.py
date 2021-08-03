from collections import OrderedDict
from itertools import count

words = OrderedDict()

for i in range(1, int(input())+1):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words.keys()))
print(*words.values(), sep = " ")
