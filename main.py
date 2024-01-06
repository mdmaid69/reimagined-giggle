import sklearn.datasets
print(sklearn.datasets.load_iris())
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))