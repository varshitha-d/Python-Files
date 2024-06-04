#to remove an element from tuple
t = tuple(map(int, input().split()))
n = int(input())
t = t[:n] + t[n+1:]
print(t)

t = tuple(map(int, input().split()))
n = int(input())
#to convert tuple to list
a = list(t)
a.remove(a[n])
# to convert list to tuple
b = tuple(a)
print(b)