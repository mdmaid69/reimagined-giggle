  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a