def next_greater_element(array):
    """
    This is the brute force method
    Worst case Time complexity is O(n*n) and space complexity is O(1)
    """
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] > array[i]:
                print(" The next greater element for {} is {}".format(array[i], array[j]))
                break
            elif j == len(array) - 1:
                print(" The next greater element for {} is -1".format(array[i]))


def next_greater_element_optimal(array):
    """
    Approach:
    1. Initialize stack with first element in array
    2. Loop through the array
        - If current number is less than one in stack top
            - push into the stack
        - if current number is more
            - print next greater element of stack top is current and pop the stack top
            - compare with all elements in stack
                - if current is greater
                    - pop the element
            - push current element to stack
    Time complexity is O(N) and Space complexity is O(N)
    """
    stack = [array[0]]
    for i in range(1, len(array)):
        if array[i] < stack[-1]:
            stack.append(array[i])
        else:
            element = stack.pop()
            print("Next greater element to {} is {} ".format(element, array[i]))
            for j in range(len(stack)):
                if array[i] > stack[-1]:
                    print("Next greater element to {} is {} ".format(stack.pop(), array[i]))
            stack.append(array[i])
    for ele in stack:
        print("Next greater element to {} is -1".format(ele))


inp = [12, 8, 6, 10, 7, 9, 11, 1]
next_greater_element_optimal(inp)
