def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)