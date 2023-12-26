  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)