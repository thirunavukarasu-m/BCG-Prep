from collections import defaultdict
def group_anagrams(arr):
    cache = defaultdict(list)
    
    for i in arr:
        char = ''.join(sorted(i))
        cache[char].append(i)
        
    return list(cache.values())
    
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

