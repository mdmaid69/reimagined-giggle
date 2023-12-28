import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_power(work, time):
        return work / time