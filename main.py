import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)