def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)