def L_substring_no_repeat(s):
    if not s:
        return -1
    seen = set()
    max_length = 0
    
    position_one = 0
    
    for position_two in range(len(s)):
        while s[position_two] in seen:
            seen.remove(s[position_one])
            position_one += 1
            
        seen.add(s[position_two])
        max_length = max(max_length, (position_two-position_one) + 1)
    return max_length
    
print(L_substring_no_repeat('abcabcbb'))