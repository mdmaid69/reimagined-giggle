import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()