  def is_odd(n):
        return n % 2 != 0
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)