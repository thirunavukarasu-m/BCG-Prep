def product_except_self(arr):
    prefix = 1
    postfix = 1
    n = len(arr)
    result = [1] * n
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]
    print(arr)
    print(result)
    for i in range(n-1,-1,-1):
        result[i] *= postfix
        postfix *= arr[i]

    return result
nums = [1,2,3,4]
print(product_except_self([-1,1,0,-3,3]))
# Output: [24,12,8,6]