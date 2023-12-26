import random
def generate_random_number(start, end):
        return random.randint(start, end)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)