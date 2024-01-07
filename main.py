  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"