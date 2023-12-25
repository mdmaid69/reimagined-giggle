import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2