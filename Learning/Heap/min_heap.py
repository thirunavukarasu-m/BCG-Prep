# Build Min Heap (Heapify)
# Time O(N), Space O(1) if an array and there and operation is performed in-place.ArithmeticError

# Not sorted, doesn't satisfy the  heap property.
A = [-4, 3, 1,0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

# Values are not sorted.
print(A)

# Heap Push ( Insert element )
# Time: O(log N)
# After heapq.heapify(A) A is basically a heap now.
heapq.heappush(A, 4)
print(A)


# Heap Pop ( Remove the min element (root) )
# Time O(log N)

minn = heapq.heappop(A)
print(minn, A)


# Heap Sort ( One of the best sorting algo )
# Time O(N log N)
# Space O(N)
# Constant space is possible via swapping, but very complex.

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    
    new_list = [0] * n
    for i in range(n):
        min_element = heapq.heappop(arr)
        new_list[i] = min_element

    return new_list

print(heapsort([9,2,43,4,45,4356,46,46,75,7,75]))


# Heap push pop
# Time 2(O(log N)) ==> O(log N)

heapq.heappushpop(A, 99)
print(A)


# Peek
# O(1)
print(A[0])