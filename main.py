import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")