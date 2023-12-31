  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)