"""
One array of integers is given as input which is initially increasing and then
decreasing or it can be only increasing or decreasing, You need to find the maximum
value in the array in O(logn) Time Complexity and O(1) space complexity
"""


def find_max(array, low, high):
    if low == high:
        return array[low]
    # if there are only two elements, return the maximum of two
    if high - low == 1:
        if array[low] >= array[high]:
            return array[low]
        return array[high]
    mid = (low + high) // 2
    # array[mid - 1] < array[mid] < array[mid + 1] -> Increasing Sequence, so go right
    if array[mid - 1] < array[mid] < array[mid + 1]:
        return find_max(array, mid + 1, high)
    # array[mid - 1] > array[mid] > array[mid + 1] -> Decreasing Sequence
    elif array[mid - 1] > array[mid] > array[mid + 1]:
        return find_max(array, low, mid - 1)
    else:
        return find_max(array, mid, high)


if __name__ == '__main__':
    arr = [6, 9, 15, 25, 35, 50, 41, 29, 23, 8]
    print(find_max(arr, 0, len(arr) - 1))
