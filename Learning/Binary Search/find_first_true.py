li = [False, False, False, True, True, True, True]

def binary_search(li):
    l = 0
    r = len(li) - 1
    
    
    while l < r:
        m = l+ ((r - l) // 2)
        if li[m]:
            r = m
        else:
            l = m + 1
    return l
        
print(binary_search(li))