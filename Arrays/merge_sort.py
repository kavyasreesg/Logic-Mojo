#Split the array into two halves
#perform the merge sort on each array
#Then combine the array in sorted order
#TC : O(nlogn); SC : O(1)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1  
     
if __name__ == '__main__':
    arr = [38, 27, 43, 39, 82, 10]
    k = 3 #return third largest element
    
    merge_sort(arr)
    print(arr)
    print("{} largest elemet is : {} ".format(k, arr[k-1]))