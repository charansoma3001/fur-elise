a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

if a>b:
    if a>c:
        print(a + " is greatest")
    else:
        print(c + " is greatest")
    
else:
    if b>c:
        print(b + " is greatest")
    else:
        print(c + " is greatest")

