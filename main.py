import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def iterate_over_array(array):
        for item in array:
        print(item)