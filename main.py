import array
def get_array_item_count(array, item):
        return array.count(item)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))