import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)