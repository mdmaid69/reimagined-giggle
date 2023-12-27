import sklearn.datasets
print(sklearn.datasets.load_iris())
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)