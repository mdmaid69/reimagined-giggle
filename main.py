import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding