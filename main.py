import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)