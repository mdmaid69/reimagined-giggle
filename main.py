def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)