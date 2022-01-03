#Program to find highest most frequently occured number
arr = [0, 5, 5, 5, 4, 4, 4]
freq = dict()
for i in range(len(arr)):
    freq[arr[i]] = 0
for i in range(len(arr)):
    freq[arr[i]] += 1
maximum = max(freq.values())
for key,value in freq.items():
    if value == maximum:
        max_freq_num = key
        break
print(max_freq_num)