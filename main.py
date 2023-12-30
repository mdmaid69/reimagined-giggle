import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2