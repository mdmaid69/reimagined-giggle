  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import random
def roll_die():
        return random.randint(1, 6)