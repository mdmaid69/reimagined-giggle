n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))