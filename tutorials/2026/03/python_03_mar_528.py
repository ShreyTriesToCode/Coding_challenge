# Heap Operations in Python

import heapq

# Create a min heap
def create_min_heap():
    heap = []
    for i in range(10):
        heapq.heappush(heap, i)
    print("Min heap:", heap)

# Create a max heap
def create_max_heap():
    heap = []
    for i in range(10):
        heapq.heappush(heap, -i)
    print("Max heap:", heap)

# Heapify a list
def heapify_list(lst):
    for i in range(len(lst) // 2 - 1, -1, -1):
        _heapify(lst, i, len(lst))
    return lst

def _heapify(lst, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        _heapify(lst, largest, n)

# Heap sort
def heap_sort(lst):
    heap = lst[:]
    heapify_list(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

# Heap merge
def heap_merge(heap1, heap2):
    if not heap1 or not heap2:
        return heap1 or heap2
    if heap1[0] < heap2[0]:
        return [heap1[0]] + heap_merge(heap1[1:], heap2)
    else:
        return [heap2[0]] + heap_merge(heap1, heap2[1:])

# Heap operations example
if __name__ == "__main__":
    # Create a min heap
    create_min_heap()

    # Create a max heap
    create_max_heap()

    # Heapify a list
    lst = [12, 11, 13, 5, 6, 7]
    print("Original list:", lst)
    print("Heapified list:", heapify_list(lst))

    # Heap sort
    lst = [12, 11, 13, 5, 6, 7]
    print("Original list:", lst)
    print("Sorted list:", heap_sort(lst))

    # Heap merge
    heap1 = [1, 3, 5]
    heap2 = [2, 4, 6]
    print("Heap 1:", heap1)
    print("Heap 2:", heap2)
    print("Merged heap:", heap_merge(heap1, heap2))