  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)