  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a