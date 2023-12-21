def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)