  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
x = 10
y = 20
print("Sum:", x + y)