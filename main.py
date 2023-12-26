  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)