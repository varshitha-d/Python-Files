a = int(input("Enter the year : "))
if a%4==0 and a%100!=0:
    print("Leap year")
else:
    if(a%400==0):
        print("Leap Year")
    else: 
        print("Non-Leap Year")