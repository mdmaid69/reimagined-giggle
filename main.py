def calculate_density(mass, volume):
        return mass / volume
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a