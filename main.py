def calculate_perpetuity(payment, rate):
        return payment / rate
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a