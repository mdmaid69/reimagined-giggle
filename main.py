  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))