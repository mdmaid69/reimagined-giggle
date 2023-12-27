import array
def get_array_as_frozenset(array):
        return frozenset(array)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"