n = int(input())
if (n%4==1):
    x = 1 ^ 1^2
    print(x)
elif (n%4 == 2):
    x = (n+1)^1^2
    print(x)
elif (n%4 == 3):
    x = 0 ^ 1 ^ 2
    print(x)
elif (n%4 == 0):
    x = n ^ 1 ^ 2
    print(x)