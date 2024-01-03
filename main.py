import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def calculate_area_circle(r):
        return 3.14 * r**2