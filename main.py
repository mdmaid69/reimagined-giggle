import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"