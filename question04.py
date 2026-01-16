# problem description :
# to find the sum of elements present in a array  


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

total = 0

for i in arr:
    total = total + i

print("Sum of elements is:", total)
