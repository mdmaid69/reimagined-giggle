import array
def get_array_as_memoryview(array):
        return memoryview(array)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"