import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"