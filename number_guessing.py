import random
for i in range(20):
    a = random.randint(1, 20)

i = 5
k=0
while(i != 0):
    b = input("Guess your number")
    if int(b)>a:
        k = k+1
        print("Your guess is higher")
    elif int(b)<a:
        print("Your guess is lesser")
        k = k+1
    else:
        k = k+1
        print("Your guess is correct in try " + str(k))
        break
    i = i - 1
