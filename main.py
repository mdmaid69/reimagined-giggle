import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_density(mass, volume):
        return mass / volume