import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)