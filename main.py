import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c