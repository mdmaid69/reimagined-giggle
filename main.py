sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)