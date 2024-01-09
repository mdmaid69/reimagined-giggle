  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)