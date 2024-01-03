import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)