# Time : O(N log N)
# Space: O(N), it can be O(log N) but it is much harder


unsorted_list = [-5,3,2,1,-3,-3,7,2,2]

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    sorted_arr = [0] * n
    middle_index = n//2
    
    L = arr[:middle_index]
    R = arr[middle_index:]
    
    L = merge_sort(L)
    R = merge_sort(R)
    
    L_len = len(L)
    R_len = len(R)
    
    l,r, i = 0, 0, 0
    
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1

        i += 1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1
    
    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
        
    return sorted_arr
    
print(merge_sort(unsorted_list))