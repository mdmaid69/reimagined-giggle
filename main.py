import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())