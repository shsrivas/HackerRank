from itertools import groupby

data  = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(data)])