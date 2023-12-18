import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5