import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets