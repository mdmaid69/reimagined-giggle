def calculate_area_circle(r):
        return 3.14 * r**2
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a