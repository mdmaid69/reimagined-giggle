def calculate_roi(gain, cost):
        return (gain - cost) / cost
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a