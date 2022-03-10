import re
sentence = input("Enter a sentence: ")
word = sentence.split(" ")
print(word)
join = ("abc").join(word)
print(join)
regex = re.compile(r'([a-zA-Z]abc[A-Za-z])*')
def check(join):
    #if(re.search(regex,join)):
    if(regex.search(join)):
        print('Search successful')
    else:
        print('Search unsuccessful')

check(join)