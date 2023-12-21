  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets