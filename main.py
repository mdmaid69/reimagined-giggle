def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)