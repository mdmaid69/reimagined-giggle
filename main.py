def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)