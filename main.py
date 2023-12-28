def calculate_area_circle(r):
        return 3.14 * r**2
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a