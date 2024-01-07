import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import random
def generate_random_number(start, end):
        return random.randint(start, end)