numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))