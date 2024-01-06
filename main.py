def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a