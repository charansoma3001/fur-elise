list1No = input("Enter the no of items in list 1: ")
list2No = input("Enter the no of items in list 2: ")
list1 = []
list2 = []
print("Enter list 1 items: ")
for i in range(int(list1No)):
    #a = input()
    list1.append(input())

print("Enter list 2 items: ")
for j in range(int(list2No)):
    b = input()
    list2.append(b)

print(list1)
print(list2)

list3 = []
list3 = list1[:int(int(list1No)/2)] + list2[int(int(list2No)/2):]
print(list3)

