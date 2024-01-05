import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  def convert_to_hex(n):
        return hex(n)