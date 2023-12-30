import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"