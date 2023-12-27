def calculate_average(lst):
        return sum(lst) / len(lst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)