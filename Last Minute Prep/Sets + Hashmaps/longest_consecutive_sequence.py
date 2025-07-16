def longest_consecutive_sequence(nums):
    cache = set(nums)
    max_count = 0
    
    # nums might contain duplicates, but set doesn't. If we have nums the time limit will exceed.
    for num in cache:
        if num - 1 not in cache:
            next_num = num + 1
            length = 1
            
            while next_num in cache:
                length += 1
                next_num += 1
        
            max_count = max(max_count, length)
            
    return max_count
    
nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_consecutive_sequence(nums))