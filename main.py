import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))