import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time