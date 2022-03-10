username = "Charan"
password = "123456"

while(input("Enter your username: ") != username):
    print("Invalid username")
else:
    while(input("Enter password: ") != password):
        print("Wrong Password...\n Access Denied")
    print("Access Granted")