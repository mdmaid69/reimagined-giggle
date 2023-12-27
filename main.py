import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"