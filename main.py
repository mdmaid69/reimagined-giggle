def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a