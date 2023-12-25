def calculate_density(mass, volume):
        return mass / volume
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a