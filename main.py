import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)