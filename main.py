def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)