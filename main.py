def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)