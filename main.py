import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"