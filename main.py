def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a