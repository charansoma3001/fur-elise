number = input('Enter the number: ')
for i in range(len(number)): 
    if(number[3:4] == '-' & number[7:8] == '-'):
        for j in range(0,3):
            if(number[0:3].isdecimal() & number[4:7].isdecimal() & number[8:12].isdecimal()):
                print(number + ' is a number')

            else:
                print(number + ' is not a number')
            
    else:
        print(number + ' is not a number')
