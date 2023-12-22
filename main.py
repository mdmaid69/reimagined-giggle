  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)