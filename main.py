import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets