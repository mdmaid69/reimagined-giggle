import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"