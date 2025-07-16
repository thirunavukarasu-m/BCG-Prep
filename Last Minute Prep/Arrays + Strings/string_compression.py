# This doesn't have constant space, so fails.
from collections import Counter
def string_compression_1(arr):
    if not arr:
        return []
    cache = Counter(arr)
    result = []
    

    for i,j in cache.items():
        result.append(f"{i}")
        result.append(f"{j}")
    
    return result
    
print(string_compression_1(["a","a","b","b","c","c","c"]))


def string_compression_2(arr):
    if len(arr) < 2:
        return len(arr)
    
    insert_position = 0
    count = 1
    for i in range(1, len(arr) + 1):
        if i < len(arr) and arr[i - 1] == arr[i]:
            count += 1
        else:
            arr[insert_position] = arr[i-1]
            insert_position += 1
            if count > 1:
                for digit in str(count):
                    arr[insert_position] = digit
                    insert_position += 1
            count = 1
    
    return insert_position
    
print(string_compression_2(["a","a",'a','a','a','a','a','a','a','a','a','a','a','a','a',"b","b","c","c","c"]))

            