  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"