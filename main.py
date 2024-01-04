import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a