import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c