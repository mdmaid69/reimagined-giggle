def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)