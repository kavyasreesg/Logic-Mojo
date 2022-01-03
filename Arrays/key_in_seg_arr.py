def arr_seg():
    arr = [3, 5, 2, 4, 9, 3,
                1, 7, 3, 11, 12, 3]
    i = 0
    k = 5
    x = 2
    n = len(arr)
    while i < n:
        j = 0
        while j < k:
            if arr[i+j] == x:
                break
            j = j+1
        if j == k:
            return False
        i +=  k
        
    if i == n:
        return True

    j = i - k

    while j < n:
        if arr[j] == x:
            return True
        j += 1
        
    if j == n:
        return False

    return True

print(arr_seg())
        
    
        
    