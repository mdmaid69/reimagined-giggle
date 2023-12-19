  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a