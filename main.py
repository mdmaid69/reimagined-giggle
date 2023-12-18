import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"