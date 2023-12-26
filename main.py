import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread