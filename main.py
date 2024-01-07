import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)