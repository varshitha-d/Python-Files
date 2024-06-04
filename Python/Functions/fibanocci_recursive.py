'''def fun(n):
    if n > 0:
        print(n)
        fun(n - 1)
        print(n)
x = 5
fun(x)'''

def fibanocci(n):
    if n <= 1:
        return n
    else:
        return fibanocci(n-1) + fibanocci(n-2)

num_terms = int(input("Enter the number of terms: "))
for i in range(num_terms):
    print(f"Fibanocci({i}) = {fibanocci(i)}")