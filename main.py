import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)