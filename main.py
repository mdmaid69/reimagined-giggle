def calculate_roi(gain, cost):
        return (gain - cost) / cost
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)