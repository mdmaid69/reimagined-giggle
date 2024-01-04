import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def count_words(sentence):
        return len(sentence.split())