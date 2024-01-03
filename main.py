import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))