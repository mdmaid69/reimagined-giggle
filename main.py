def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)