def convert_to_hex(n):
        return hex(n)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)