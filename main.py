  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a