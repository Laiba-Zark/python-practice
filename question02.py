
# Problem Description Find the largest element present in the array.

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element is:", largest)
