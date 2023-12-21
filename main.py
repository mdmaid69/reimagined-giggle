import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)