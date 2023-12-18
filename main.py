import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a