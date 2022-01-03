"""
Find the largest rectangular area possible in a given histogram
"""


def max_area(array):
    stack = list()
    index = 0
    maxarea = 0
    while index < len(array):
        if (not stack) or (array[stack[-1]] <= array[index]):
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (array[top] * ((index - stack[-1] - 1) if stack else index))
            maxarea = max(area, maxarea)

    while stack:
        top = stack.pop()
        area = array[top] * ((index - stack[-1] - 1) if stack else index)
        maxarea = max(area, maxarea)
    return maxarea


array_in = [6, 2, 5, 4, 5, 1, 6]
print("Maximum area is :", max_area(array_in))
