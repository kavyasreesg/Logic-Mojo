"""
Given an array nums,write a function to move all 0's to the end of it while
maintaining the relative order of the non zero elements in O(n) Time complexity and
O(1) space complexity with single traversal allowed
Algorithm:
Maintain cnt variable
Loop through the array
 - Whenever a non zero element is encountered swap with the left most zeroth element
"""
array = [1, 3, 0, 0, 0, 0, 9, 0]
cnt = 0
for j in range(len(array)):
    if array[j] != 0 and j != cnt:
        array[j], array[cnt] = array[cnt], array[j]
        cnt += 1
    elif array[cnt] != 0:
        cnt += 1

print(array)