numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)