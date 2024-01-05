import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))