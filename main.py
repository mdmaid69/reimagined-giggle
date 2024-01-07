import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets