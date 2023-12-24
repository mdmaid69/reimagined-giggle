import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"