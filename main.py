def calculate_area_circle(r):
        return 3.14 * r**2
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a