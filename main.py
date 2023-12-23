import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)