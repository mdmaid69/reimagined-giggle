import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)