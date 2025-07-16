from collections import defaultdict


def L_substring_with_atmost_k_distinct_chars(s,k):
    start, end, max_length = 0,0,0
    seen = defaultdict(int)
    
    
    while end < len(s):
        if s[end] not in seen:
            k -= 1
        seen[s[end]] = end
        
        while k < 0:
            if seen[s[start]] == start:
                k += 1
            start += 1
        max_length = max(max_length, end - start + 1)
        end += 1
    return max_length
print(L_substring_with_atmost_k_distinct_chars("ecebaa", 2))