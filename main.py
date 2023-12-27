import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a