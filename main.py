import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  def calculate_area_triangle(b, h):
        return 0.5 * b * h