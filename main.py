import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_roi(gain, cost):
        return (gain - cost) / cost