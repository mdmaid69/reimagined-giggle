import logging
def log_message(message):
        logging.info(message)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))