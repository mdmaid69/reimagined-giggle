import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_energy(mass, c=3*10**8):
        return mass * c**2