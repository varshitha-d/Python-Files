L = input().split(" ")
b = []
for i in L:
    if L.count(i)%2!=0 and i not in b:
        b.append(i)
print(b)