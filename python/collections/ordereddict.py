from collections import OrderedDict

oDict = OrderedDict()
n = int(input())
for i in range(1, n+1):
    item = input().rsplit(None, 1)
    if item[0] in oDict:
        oDict[item[0]] = int(item[1]) + oDict[item[0]]
    else:
        oDict[item[0]] = int(item[1])

for key, value in oDict.items():
    print(key, value)