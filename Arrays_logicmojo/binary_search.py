"""
Time complexity is O(logN) where N is size of the array
"""


def binary_search(array_in, low, high, element):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array_in[mid] == element:
        return mid
    elif element > array_in[mid]:
        return binary_search(array_in, mid + 1, high, element)
    else:
        return binary_search(array_in, low, mid - 1, element)


if __name__ == "__main__":
    array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("element is found at", binary_search(array, 0, len(array) - 1, 5))
