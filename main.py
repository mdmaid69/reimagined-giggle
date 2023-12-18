import random
def generate_random_choice(choices):
        return random.choice(choices)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)