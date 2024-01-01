import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()