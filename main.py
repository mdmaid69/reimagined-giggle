def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a