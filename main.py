  def reverse_list(lst):
        return lst[::-1]
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)