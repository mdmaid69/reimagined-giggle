def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)