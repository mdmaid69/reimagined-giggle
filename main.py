import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_average(lst):
        return sum(lst) / len(lst)