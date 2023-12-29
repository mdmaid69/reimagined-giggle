  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a