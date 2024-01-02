import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)