def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))