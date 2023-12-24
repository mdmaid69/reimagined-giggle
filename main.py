def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a