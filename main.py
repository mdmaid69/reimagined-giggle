def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a