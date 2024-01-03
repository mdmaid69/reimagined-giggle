import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets