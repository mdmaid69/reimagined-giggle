import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_area(radius):
        return 3.14 * radius * radius