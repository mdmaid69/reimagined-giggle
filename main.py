  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)