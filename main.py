import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)