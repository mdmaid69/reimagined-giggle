import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets