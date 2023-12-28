import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)