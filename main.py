import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)