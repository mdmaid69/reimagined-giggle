import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets