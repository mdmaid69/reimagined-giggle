import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)