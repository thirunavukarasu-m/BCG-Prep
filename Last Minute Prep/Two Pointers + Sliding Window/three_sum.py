def three_sum(arr, target=None):
    if len(arr) < 3:
        return []
    arr.sort()
    initial_position = 0
    result = []
    while initial_position < len(arr) - 2:
        if initial_position > 0 and arr[initial_position] == arr[initial_position - 1]:
            initial_position += 1
            continue
        left, right = initial_position + 1,len(arr) - 1
        while left < right:
            current_sum = arr[initial_position] + arr[left] + arr[right]
            if current_sum == 0:
                result.append([arr[initial_position] , arr[left] , arr[right]])
                
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
        initial_position += 1
        
    
    return result
print(three_sum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10], 0))