import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_average(lst):
        return sum(lst) / len(lst)