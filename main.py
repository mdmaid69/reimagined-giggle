import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps