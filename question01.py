
# Problem Description Given an array of integers, reverse the order of its elements.
# input is 
# 5
# 1 2 3 4 5g
n = int(input(" enter the integer you want to reverse:"))
arr = list(map(int, input().split()))

arr.reverse()

print(*arr)
