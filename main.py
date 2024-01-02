import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a