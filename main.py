  def convert_to_hex(n):
        return hex(n)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)