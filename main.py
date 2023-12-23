import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal