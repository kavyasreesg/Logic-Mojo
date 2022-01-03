import sys
arr = [1,1,13,4,5,6,7,8,6,5]
max = -sys.maxsize
min = sys.maxsize
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min,max)

#Time complexity O(N)