from collections import namedtuple

n, sclass = int(input()), namedtuple('Students', input().split())
a = 0

s = [getattr(sclass(*input().split()), 'MARKS')  for i in range(n)]

# print(a)
print("{:.2f}".format(sum(map(int, s))/n))
