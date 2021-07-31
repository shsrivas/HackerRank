n = int(input())
s = set(map(int, input().split()))
t = int(input())
print(t)
for i in range(t):
    print(i)
    st = input()
    if st == 'pop':
        s.pop()
    else:
        st,m = st.split()
        if st == 'discard':
            s.discard(int(m))

        elif st == 'remove':
            s.remove(int(m))

print(sum(s))
