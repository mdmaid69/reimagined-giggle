  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)