def find_difference(list1, list2):
        return set(list1) - set(list2)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))