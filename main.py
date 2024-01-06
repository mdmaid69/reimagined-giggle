import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)