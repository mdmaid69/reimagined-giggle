def calculate_average(lst):
        return sum(lst) / len(lst)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a