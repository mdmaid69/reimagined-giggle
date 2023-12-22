def calculate_area_rectangle(l, w):
        return l * w
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a