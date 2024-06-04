def numbers(n):
    s = "" 
    for i in range(n, 0, -1):  
        s += str(i)
    return s

num = int(input())
print(numbers(num))