import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))