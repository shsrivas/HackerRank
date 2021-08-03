from collections import Counter

n = int(input())
sizes = Counter(map(int, input().split()))
purchase = int(input())

total =0
plist = []

for i in range(purchase):
    plist = list(map(int, input().split()))
    if sizes[plist[0]]:
        total += plist[1]
        sizes[plist[0]] -= 1


print(total)
