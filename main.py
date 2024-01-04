def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a