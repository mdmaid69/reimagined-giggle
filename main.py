import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"