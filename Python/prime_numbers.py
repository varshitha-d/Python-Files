n = int(input())
if (n>=2):
    for i in range(2,n):
        if(n%i==0):
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
elif n==1:
    print("Neither prime nor composite")
