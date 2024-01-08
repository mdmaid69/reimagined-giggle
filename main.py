import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)