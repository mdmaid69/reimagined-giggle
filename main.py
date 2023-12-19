def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))