import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps