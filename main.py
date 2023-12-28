import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"