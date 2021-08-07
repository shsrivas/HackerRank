n, m = map(int, input('enter your doormat size').split())
c = '.|.'
print(type(n))

#for the top design
for i in range(1, n, 2):
    a = (c*i).center(m-i, '-')
    print(a)



print('WELCOME'.center(m, '-'))

for i in range(n-2, -1, -2):
    print((c * i).center(m, '-'))


