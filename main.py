import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps