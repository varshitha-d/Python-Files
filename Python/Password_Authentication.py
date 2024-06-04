username = input("Enter Username : ")
count = 3

if username == "Admin" :
    while count > 0:
        Password = input("Enter Password : ")
        if Password == "password123":
            print("Credentials are correct. You are logged in.")
            break
        else:
            count -= 1
            if count > 0:
                print("Wrong password. You have ", count, " more attempts left.")
            elif count == 0:
                print("Wrong Credentials. Account locked.")
else:
    print("Invalid Usermane")