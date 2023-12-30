import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"