import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)