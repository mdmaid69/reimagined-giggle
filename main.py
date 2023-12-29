import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets