import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)