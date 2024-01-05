def calculate_average(lst):
        return sum(lst) / len(lst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)