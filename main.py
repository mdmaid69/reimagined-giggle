import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a