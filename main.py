import array
def append_to_array(array, item):
        array.append(item)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)