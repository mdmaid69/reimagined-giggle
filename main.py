import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"