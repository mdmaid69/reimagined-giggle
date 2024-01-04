import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5