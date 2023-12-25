import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)