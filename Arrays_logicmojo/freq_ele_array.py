"""
Array of length n having integers 1 to n with some elements being repeated. count
frequencies of all elements from 1 to n in Time complexity O(n) and Space
Complexity O(1)
"""
array = [1,2,2,2,2,5,5]
n = len(array)
for i in range(n):
    array[i] -= 1 # [0,1,1,0,2,5,5]; Since array elements index starts from 0

for i in range(n):
    if array[i] <= len(array)-1:
        array[array[i]] = array[array[i]]+n
    else:
        array[array[i]] = array[array[i]] % n

for i in range(n):
    array[i] = array[i]//n
    print("{} occurred {} times".format((i+1), array[i]))
    if array[i] >= (len(array)//2)+1:
        print("{} is majority number".format(i+1))