def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)