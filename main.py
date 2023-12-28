import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))