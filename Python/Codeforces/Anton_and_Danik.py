n = int(input())
won = input()
count1 = 0
count2 = 0
for i in won:
    if i=="A":
        count1 += 1
    elif i=="D":
        count2 += 1
if count1>count2:
    print("Anton")
elif count1<count2:
    print("Danik")
else:
    print("Friendship")


'''n=int(input())
s=str(input())
anton=s.count('A')
danik=s.count('D')

if anton> danik:
    print("Anton")
elif danik>anton:
    print("Danik")
else:
    print("friendship")'''