import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)