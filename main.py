import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))