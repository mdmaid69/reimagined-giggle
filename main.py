import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)