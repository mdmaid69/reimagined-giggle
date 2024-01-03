import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def calculate_area_triangle(b, h):
        return 0.5 * b * h