  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)