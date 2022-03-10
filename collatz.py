num = int(input("Enter number"))
print(num)

def collatz(num):
    if(num%2==0):
        num = num / 2
        print(num)
    else:
        num = 3*num+1
        