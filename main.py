import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"