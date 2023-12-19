import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)