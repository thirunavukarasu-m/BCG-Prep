li = [-4, -3, -2, -1, 0, 2,3,5,6,7,8]

def binary_search(li, target):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
    
print(binary_search(li, 5))