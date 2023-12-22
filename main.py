import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets