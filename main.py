def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)