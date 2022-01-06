"""
we have an array, we have to find an element before which all elements are less
than it, and after which all are greater than it. Finally return the index
of the element, if there is no such element, return -1
Time complexity is O(n) and space complexity is O(n)
Refer running notes for algo
"""
import sys

array = [6,2,5,4,7,9,11,8,10]
n = len(array)
# start = n-1
# for i in range(n-1, 0, -1):
#     if array[start] > array[start - 1] > array[start - 2]:
#         break
#     start -= 1
# j = start-1
# array = sorted(array[:j-1], reverse=True)+array[j-1:j+1]+sorted(array[j+1:],reverse=True)
# print(array)
# start = 0
# end = n-1
# for i in range(n):
#     if array[start] < array[j] < array[end]:
#         break
#     j -= 1
# print(j)
left = [sys.maxsize]
right = []
for i in range(1, n):
    left.insert(i, max(array[:i]))
m = n
for j in range(len(array)-1):
    right.insert(j, min(array[m-1:]))
    m -= 1
right.reverse()
right.append(-sys.maxsize)
for i in range(len(array)-1):
    if left[i] < array[i] < right[i]:
        break
print(i)