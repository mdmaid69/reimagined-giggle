import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2