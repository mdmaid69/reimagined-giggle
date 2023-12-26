import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"