import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)