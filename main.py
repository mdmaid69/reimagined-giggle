import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets