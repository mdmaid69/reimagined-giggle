import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)