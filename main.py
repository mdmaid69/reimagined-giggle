import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def calculate_area_triangle(b, h):
        return 0.5 * b * h