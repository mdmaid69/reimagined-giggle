import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)