def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a