  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)