  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"