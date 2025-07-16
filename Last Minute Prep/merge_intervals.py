def merge_intervals(arr):
    stack = []
    arr.sort()
    for i in arr:
        if stack and stack[-1][1] >= i[0]:
            stack[-1] = [min(stack[-1][0], i[0]), max(stack[-1][1], i[1])]
        else:
            stack.append(i)
        
    return stack

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))