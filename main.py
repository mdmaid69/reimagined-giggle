def calculate_force(mass, acceleration):
        return mass * acceleration
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a