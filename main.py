import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"