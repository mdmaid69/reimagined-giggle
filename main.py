import collections
def create_user_dict():
        return collections.UserDict()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)