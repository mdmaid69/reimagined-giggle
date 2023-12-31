import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities