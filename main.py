import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread