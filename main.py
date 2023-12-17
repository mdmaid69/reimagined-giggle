def calculate_force(mass, acceleration):
        return mass * acceleration
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a