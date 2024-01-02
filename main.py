  def remove_duplicates(lst):
        return list(set(lst))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a