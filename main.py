import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2