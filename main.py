def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a