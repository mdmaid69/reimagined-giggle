import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()