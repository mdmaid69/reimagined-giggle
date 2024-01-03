  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}