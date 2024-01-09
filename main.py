import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets