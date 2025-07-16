def two_sum_sorted(arr, target):
    if not arr:
        return []
        
    left, right = 0,len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
            
    return []
print(two_sum_sorted([2,7,11,15], 9))