'''One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and 
the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. 
They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.
Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way 
that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are 
equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help 
them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part 
of positive weight.'''

weight =  int(input("Enter the weight of the watermelon : "))
if weight <= 100:
    if weight > 2 and weight%2==0 :
        print("YES")
        h=weight/2
        if h%2!=0:
            print("weights of 2 pieces are : ",int(h+1),int(h-1))
        else:
            print("weights of 2 pieces are : ",int(h),int(h))
    else:
        print("NO")
else:
    print("Weight above 100")