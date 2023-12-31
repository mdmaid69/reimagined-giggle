  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)