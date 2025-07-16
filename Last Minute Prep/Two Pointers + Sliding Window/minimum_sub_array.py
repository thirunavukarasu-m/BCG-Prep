def minimum_sub_array(arr, target):
    min_length = float('inf')
    summ = 0
    l = 0
    
    for r in range(len(arr)):
        summ += arr[r]
        
        while summ >= target:
            min_length = min(min_length, r-l + 1)
            summ -= arr[l]
            l += 1
    return min_length if min_length < float('inf') else 0
    
print(minimum_sub_array([2,3,1,2,4,3], 7))