from itertools import combinations
from itertools import groupby

n = int(input())
alp = input().split()
k = int(input())

com = list(combinations([x for x in range(1, n+1)], k))

l = []
j =1
for i in alp:
    if i == 'a':
        l.append(j)
        j+=1

count = 0
for k, c in groupby(com):
    for i in l:
        if i in k:
            count+=1
            break
        else:
            continue


print("{:.3f}".format(count/len(com)))
