  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list