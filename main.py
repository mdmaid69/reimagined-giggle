import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity