L = list(map(int,input().split(" ")))
a,b = map(int,input().split(" "))
Product = 1
for i in L:
    if i>=a and i<=b:
        Product *= i
print(Product)