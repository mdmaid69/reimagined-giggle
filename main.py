  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)