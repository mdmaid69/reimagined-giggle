numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)