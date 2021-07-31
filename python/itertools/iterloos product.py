from itertools import permutations
# a = map(int, input().split(" "))
# b = map(int, input().split(" "))
#
#
# x = list(product(a,b))
#
# # print("this is one:", ",".join(map(str, x)))
# print("this is two:", *x)
#
# # permutation

# per = input().split(" ")
#
# x = list(permutations(per[0], int(per[1])))
# x.sort()
#
# for i in x:
#      print("".join(list(i)))

# COMBINATIONS----------------------------------------------------
from itertools import combinations

per,n = input().split(" ")
print(*list(map(''.join, sorted(combinations(per, int(n))))), sep='\n')
for i in range(1, int(n)+1):
    print(*list(map(''.join, combinations(sorted(per), i))), sep='\n')

# print(*list(map(''.join, for i in range(1, int(n)+1) sorted(combinations(per, i)))), sep='\n')