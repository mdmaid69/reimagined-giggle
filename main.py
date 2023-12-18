import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity