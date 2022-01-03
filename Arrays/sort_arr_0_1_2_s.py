arr = [0, 1, 2, 0, 1, 2]
count_0 = 0
count_1 = 0
count_2 = 0
for i in range(len(arr)):
    if arr[i] == 0:
        count_0 += 1
    if arr[i] == 1:
        count_1 += 1
    if arr[i] == 2:
        count_2 += 1
j = 0
while count_0 > 0:
    arr[j] = 0
    j += 1
    count_0 -= 1
while count_1 > 0:
    arr[j] = 1
    j += 1
    count_1 -= 1
while count_2 > 0:
    arr[j] = 2
    j += 1
    count_2 -= 1
print(arr)