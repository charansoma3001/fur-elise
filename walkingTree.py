import os
for folderName, subfolders, filenames in os.walk('D:\\Work'):
    print('The current folder is ' + folderName)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        fileList1 = filename.split(".")



    print('')