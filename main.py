def calculate_acceleration(speed, time):
        return speed / time
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a