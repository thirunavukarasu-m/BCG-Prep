def subarray_sum_equals_k(arr, k):
    prefix_sum = 0
    cache = {0:1}
    count = 0
    for i in arr:
        prefix_sum += i
        if (prefix_sum - k) in cache:
            count += cache[prefix_sum - k]
        cache[prefix_sum] = cache.get(prefix_sum, 0) + 1

    return count
nums = [1,1,1]
k = 2

print(subarray_sum_equals_k(nums,k))