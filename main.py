sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)