def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)