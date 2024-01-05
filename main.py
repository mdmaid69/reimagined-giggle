  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a