import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)