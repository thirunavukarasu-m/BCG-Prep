def move_zeroes(arr):
    position = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1
    return arr

print(move_zeroes([0,1,0,3,12]))