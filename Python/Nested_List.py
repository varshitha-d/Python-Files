L = [12, 33.4, "abc", [87,'xyz',[1,2]], 10, [1,2]]
print(L)
print(L[3])
print(L[3][2])
print(L[3][2][0])

L = [1,2,['ABC','HI',452],5,6,[120]]
L[5] += [20]
print(L[5])

L = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(L)