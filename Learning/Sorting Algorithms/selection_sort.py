# Time O(N^2)
# Space O(1) In Place swap

unsorted_list = [-5,3,2,1,-3,-3,7,2,2]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        # We already have the min_idex which points to i, so we can start from i+1.
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
print(selection_sort(unsorted_list))