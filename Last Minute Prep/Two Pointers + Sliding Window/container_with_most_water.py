def container_with_most_water(arr):
    max_area = 0
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        width, height = right - left, min(arr[left], arr[right])
        max_area = max(max_area, width * height)
        
        # We have to move based on which line height is small.
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
    
print(container_with_most_water([1,8,6,2,5,4,8,3,7]))