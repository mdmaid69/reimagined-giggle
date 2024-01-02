def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a