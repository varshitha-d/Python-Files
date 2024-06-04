n = int(input())
d = {k:k*k for k in range(1,n+1)}
print(d)

#alternative
n=int(input(""))
d=dict
for x in range(1,n+1):
    d[x]=x*x
print(d)