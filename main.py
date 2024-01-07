import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity