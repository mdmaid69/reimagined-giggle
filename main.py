  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"