import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)