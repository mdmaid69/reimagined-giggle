import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"