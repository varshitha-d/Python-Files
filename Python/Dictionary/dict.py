d = {1:'hi','a':123, 100:32.4, 10:'abc',11:'cds'}
#accesing element using key
print(d[1])
print(d['a'])
print(d[100])
#accessing element using get()
print(d.get('a'))
#accessing dictionary using loops
for i in d:
    print(i,":",d[i])

#del d[1]
d.popitem()
print(d)

#fromkeys()
d = {'a','b','c','d'}
d = dict.fromkeys(d,10)
print(d)

#setdefault
d = {1:'hi','a':123, 100:32.4}
print(d.setdefault('a'))
print(d.setdefault('b'))
print(d)
print(d.setdefault('c',200))
print(d.setdefault('d'))
print(d)