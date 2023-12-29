  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b