
def intersection_of_array(arr_1, arr_2):
    m,n = len(arr_1), len(arr_2)
    left = False
    seen = set()
    result = []
    if m > n:
        cache = set(arr_1)
    else:
        cache = set(arr_2)
        left = True
    if left:
        for i in arr_1:
            if i in cache and i not in seen:
                seen.add(i)
                result.append(i)
    else:
        for i in arr_2:
            if i in cache and i not in seen:
                seen.add(i)
                result.append(i)

    
    return result