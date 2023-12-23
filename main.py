import sklearn.datasets
print(sklearn.datasets.load_iris())
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)