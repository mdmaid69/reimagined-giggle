def calculate_area(radius):
        return 3.14 * radius * radius
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a