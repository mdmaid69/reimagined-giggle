import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets