import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  def convert_to_hex(n):
        return hex(n)