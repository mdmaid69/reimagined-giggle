def calculate_acceleration(speed, time):
        return speed / time
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a