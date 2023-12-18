import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())