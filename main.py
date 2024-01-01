import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"