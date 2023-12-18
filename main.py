def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)