from typing import Text


line1 = input("Enter a sentence: ")
count = 0
    
wordAtoZ = [line1.split()]

print(wordAtoZ)
for i,word in wordAtoZ:
    print(word)
    if(word[int(i)][0] == 'a' and word[i][3] == 'z'):
        count = count + 1

print(count)

