  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)