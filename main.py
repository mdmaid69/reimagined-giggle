import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"