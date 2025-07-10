# Time O(N^2)
# Space O(1) In Place swap

unsorted_list = [-5,3,2,1,-3,-3,7,2,2]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                # This prevents going further back.
                break
    return arr
    
print(insertion_sort(unsorted_list))