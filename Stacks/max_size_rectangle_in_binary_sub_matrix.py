"""
Problem : Find maximum size rectangle in Binary Sub Matrix
Approach :
    - Loop through each element in matrix starting from second and add previous row's
    element to current element if current element is 1.
    - This way we can get how many consecutive 1's are present previously
    - Then find the histogram area for each row in the matrix
    - Finally return the maximum area
"""


def max_area(array):
    stack = list()
    area_max = 0
    index = 0
    while index < len(array):
        if (not stack) or (array[stack[-1]] <= array[index]):
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = array[top] * (index - stack[-1] - 1) if stack else index
            area_max = max(area, area_max)
    while stack:
        top = stack.pop()
        area = array[top] * (index - stack[-1] - 1) if stack else index
        area_max = max(area, area_max)
    return area_max


def matrix_max_area(matrix):
    area_list = []
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] += matrix[row - 1][col]
        area_list.append(max_area(matrix[row]))

    print(max(area_list))


matrix_max_area([
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
])
