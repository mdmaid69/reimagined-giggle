import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a