import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps