  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)