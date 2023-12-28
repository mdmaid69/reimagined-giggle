  def is_even(n):
        return n % 2 == 0
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)