  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)