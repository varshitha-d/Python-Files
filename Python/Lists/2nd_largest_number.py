L = [10, 11, 15, 11, 9 , 8]
a = max(L)
b = L[0]
for i in range(len(L)):
    if i > b and i < a:
        m = i
print(m)