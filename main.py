  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)