  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)