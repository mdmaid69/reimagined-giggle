import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)