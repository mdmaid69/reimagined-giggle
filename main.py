import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)