def calculate_volume(length, width, height):
        return length * width * height
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)