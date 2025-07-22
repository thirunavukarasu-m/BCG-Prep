numbers = [1,23,156,1650,651,165,32]
# Output - 3 ----> 23 - 32, 156 - 165, 156 - 651

def mystical_transformation(numbers):
    result = 0
    
    cache = {}
    for i in numbers:
        string = str(i)
        if len(string) not in cache:
            new_string = ''.join(sorted(string))
            cache[len(string)] = set()
            cache[len(string)].add(new_string)
        else:
            new_string = ''.join(sorted(string))
            if new_string in cache[len(string)]:
                result += 1
            
            cache[len(string)].add(new_string)
    print(cache)
    return result
    
print(mystical_transformation(numbers))