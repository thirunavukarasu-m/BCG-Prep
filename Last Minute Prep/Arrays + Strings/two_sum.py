def two_sum(numbers, target):
    if not numbers:
        return []
        
    cache = {}
    for i,j in enumerate(numbers):
        diff = target - j
        if diff in cache:
            return [i, cache[diff]]
        else:
            cache[j] = i
        
    return []