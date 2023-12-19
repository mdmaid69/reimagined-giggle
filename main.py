import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets