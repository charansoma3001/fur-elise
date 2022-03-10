number = int(input("Enter product to be found: "))
arr = []
print("Enter the array numbers: ")

for i in range(0,10):
    arr.append(int(input()))

print(arr)

count = 0

x = len(arr)

for i in range(0, len(arr)-1):
    for j in range(1, len(arr)):
        if arr[i]*arr[j] == number:
            count = count + 1

print(count)
        