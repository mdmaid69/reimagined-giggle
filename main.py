import array
def convert_array_to_list(array):
        return array.tolist()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"