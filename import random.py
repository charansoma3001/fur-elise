import random, sys
for i in range(5):
    if i == 2:
        sys.exit()
    else:
        print(random.randint(1, 10))