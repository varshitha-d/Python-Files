a = {10,20}
b = {10,20,30,40}
print(a.issubset(b))
print(b.issuperset(a))

s = { a for a in range(10) if a%2==0}
print(s)