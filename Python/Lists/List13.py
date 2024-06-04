L = list(map(int,input().split(" ")))
evens = []
odds = []
for i in L:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
evens.sort(reverse = True)
odds.sort()
L1 = evens + odds
print(L1)

'''L = list(map(int,input().split(" ")))
b = []
L.sort()
for i in L:
    if i % 2 == 0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)'''