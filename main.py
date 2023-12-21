import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def remove_duplicates(lst):
        return list(set(lst))