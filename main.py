import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)