L = list(map(int,input().split()))
b = []
for i in range(len(L)):
    if i not in b:
        b.append(L[i])
b.sort(reverse = True)
print(sum(b[:3]))