import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets