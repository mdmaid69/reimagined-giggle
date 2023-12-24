def find_unique_words(sentence):
        return set(sentence.split())
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)