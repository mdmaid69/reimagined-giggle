import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2