import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  def remove_duplicates(lst):
        return list(set(lst))