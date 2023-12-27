  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
n = 10
print("Powers of 2:", [2**x for x in range(n)])