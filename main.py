import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"