import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def reverse_list(lst):
        return lst[::-1]