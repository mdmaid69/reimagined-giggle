  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
n = 10
print("Square numbers:", [x**2 for x in range(n)])