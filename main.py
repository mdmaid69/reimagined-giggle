def convert_to_binary(n):
        return bin(n)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)