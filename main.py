def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a