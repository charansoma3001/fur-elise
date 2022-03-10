def character(str, c, n):
    if (str == None):
        print(None)
    else:
        if(len(str) % 2 == 0):
            letters = list(str)
            for i in range(0, n):
                letters.insert(len(str)//2, c)
            
        print(''.join(letters))
        

a = 'xyzxyz'
b = 'r'
c = 7
character(a, b, c)