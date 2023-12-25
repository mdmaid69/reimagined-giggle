import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"