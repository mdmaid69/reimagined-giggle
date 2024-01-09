import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets