text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)