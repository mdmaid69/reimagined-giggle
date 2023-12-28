import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding