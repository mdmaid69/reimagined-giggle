import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities