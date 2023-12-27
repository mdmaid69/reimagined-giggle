import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities