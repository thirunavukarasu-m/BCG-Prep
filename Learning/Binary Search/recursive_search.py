li = [-5,-3,-2,1,3,5]


def binary_search(li, target, left, right):
    # mid = (left + right) // 2
    mid = left + (right - left) // 2
    if left > right:
        return -1
    if li[mid] == target:
        return mid
    elif li[mid] < target:
        return binary_search(li, target, mid + 1, right)
    else:
        return binary_search(li, target, left, mid - 1)
        

print(binary_search(li, 5, 0, len(li) - 1))