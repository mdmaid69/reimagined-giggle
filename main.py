def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)