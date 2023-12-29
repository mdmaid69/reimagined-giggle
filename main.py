import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_energy(mass, c=3*10**8):
        return mass * c**2