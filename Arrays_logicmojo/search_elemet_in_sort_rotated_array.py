"""
Algorithm to find an element in sorted and clockwise rotated array
Tip : Make use of binary search algorithm
"""


def find_element(arr, low, high, element):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == element:
        return mid

    if arr[low] <= arr[mid]:
        if (element <= arr[mid]) and (element >= arr[low]):
            return find_element(arr, low, mid - 1, element)
        return find_element(arr, mid + 1, high, element)
    if arr[high] >= element >= arr[mid + 1]:
        return find_element(arr, mid + 1, high, element)
    return find_element(arr, low, mid - 1, element)


if __name__ == '__main__':
    array = [3, 4, 5, 6, 7, 8, 1, 2]
    print(find_element(array, 0, len(array) - 1, 4))
