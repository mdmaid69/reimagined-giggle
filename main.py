  def calculate_area_triangle(b, h):
        return 0.5 * b * h
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a