import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps