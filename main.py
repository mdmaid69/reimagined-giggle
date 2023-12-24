  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)