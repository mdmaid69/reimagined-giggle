def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a