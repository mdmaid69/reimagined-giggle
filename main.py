def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a