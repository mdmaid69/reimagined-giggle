def calculate_volume(length, width, height):
        return length * width * height
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a