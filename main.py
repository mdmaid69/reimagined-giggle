import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps