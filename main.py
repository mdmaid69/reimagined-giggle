import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"