import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2