"""
When you encounter 2, swap with the right most part of the array, end index --
When you encounter 0, swap with the left most part of the array, mid ++, start ++
else mid ++
O(n) and O(1) - Time and Space complexity
or Use counting sort
count no of 0's and 1's and 2's
and arrange the array with elements of their respective count
"""
array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
start = 0
mid = 0
end = len(array) - 1
for index in range(len(array)):
    if array[mid] == 2:
        array[mid], array[end] = array[end], array[mid]
        end -= 1
    elif array[mid] == 0:
        array[start], array[mid] = array[mid], array[start]
        mid += 1
        start += 1
    else:
        mid += 1
print(array)

array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
a = array.count(0)
b = array.count(1)
c = array.count(2)
i = 0
while a > 0:
    array[i] = 0
    a -= 1
    i += 1

while b > 0:
    array[i] = 1
    b -= 1
    i += 1

while c > 0:
    array[i] = 2
    c -= 1
    i += 1
print(array)