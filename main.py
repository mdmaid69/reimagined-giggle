import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))