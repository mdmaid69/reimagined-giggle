  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])