import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"