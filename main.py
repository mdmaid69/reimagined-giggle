import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)