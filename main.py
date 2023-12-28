import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)