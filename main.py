def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a