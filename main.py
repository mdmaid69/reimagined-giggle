  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}