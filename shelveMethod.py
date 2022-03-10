import shelve
cats = ['Zoophie', 'dogs', 'animals']
shelfFile = shelve.open('mydata')
shelfFile['cats'] = cats
shelfFile.close()