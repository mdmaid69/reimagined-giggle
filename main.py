  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)