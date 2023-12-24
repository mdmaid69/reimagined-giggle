import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps