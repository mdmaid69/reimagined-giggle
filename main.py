import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)