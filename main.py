import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)