  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)