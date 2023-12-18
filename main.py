def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)