def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a