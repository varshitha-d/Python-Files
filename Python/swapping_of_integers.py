#swapping of integers using regular method
a = 4
b = 5
a,b = b,a
print(a)
print(b)

#swapping of integers using bitwise operators
a = 10
b = 20
c = a^b
a = a^c
b = b^c
print(a)
print(b)

#or
a = 5
b = 7
a = a^b
b = a^b
a = a^b
print(a)
print(b)

#1->11
a = 10
print(-(~b))

#checking whether the given number is odd or even
a = int(input("Enter a number : "))
if (a&1 == 0):
    print("even")
else:
    print("odd")

print(~5)

#left shift
print(10<<2)

#right shift
print(10>>2)