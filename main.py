import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_average(lst):
        return sum(lst) / len(lst)