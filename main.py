def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)