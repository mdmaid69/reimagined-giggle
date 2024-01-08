import array
def iterate_over_array(array):
        for item in array:
        print(item)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a