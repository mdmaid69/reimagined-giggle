import array
def convert_array_to_unicode(array):
        return array.tounicode()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)