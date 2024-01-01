  def square_number(x):
        return x**2
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)