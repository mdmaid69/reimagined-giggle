import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"