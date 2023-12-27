def calculate_force(mass, acceleration):
        return mass * acceleration
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a