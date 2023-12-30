def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a