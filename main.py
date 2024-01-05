def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a