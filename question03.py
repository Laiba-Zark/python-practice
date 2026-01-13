# Problem Description Find the smallest element in the array.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element is:", smallest)
