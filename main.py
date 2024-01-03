def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a