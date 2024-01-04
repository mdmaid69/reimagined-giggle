def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a