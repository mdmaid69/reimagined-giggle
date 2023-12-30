def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)