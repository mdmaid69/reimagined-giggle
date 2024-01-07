  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities