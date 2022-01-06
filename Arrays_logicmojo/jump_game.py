"""
Given an array of non negative integers, you are initially positioned at the first index
of the array. Each element in the array represents your maximum jump length at that
position. Determine if you are able to reach the last index in O(n) time complexity and
O(1) space complexity
Algo:
    - Take two pointers pointing to first element of the array
    - Take a variable to keep track of jumps
    - Loop through the array
        - decrement the values in two pointers
        - If index reaches the last element, return jump
        - Check whether the current element is higher than second pointer if so assign current element
            as second pointer; This is to optimize the number of jumps
        - if first pointer reaches 0, increment jump and assign second pointer to first
"""


def num_jumps():
    array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    jump = 1
    a = b = array[0]
    for i in range(1, len(array)):
        if i == len(array) - 1:
            return jump
        a -= 1
        b -= 1
        if array[i] > b:
            b = array[i]
        if a == 0:
            jump += 1
            a = b
    return jump


print(num_jumps())
