n1 = ['Python', 'Flank', 'Django', 'Tkinter']
n2 = n1
n3 = n1[:2]
print(n1)
print(n2)
print(n3)
n2[0] = 'Scipy'
n3[1] = 'Numpy'
print(n1)
print(n2)
print(n3)

s = 10
for i in (n1, n2, n3):
    if i[0] == 'Python':
        s += 1
    if i[1] == 'Python':
        s += 2
print(s)