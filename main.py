def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)