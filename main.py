import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)