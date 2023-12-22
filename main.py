import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_roi(gain, cost):
        return (gain - cost) / cost