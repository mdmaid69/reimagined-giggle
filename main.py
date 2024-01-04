def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)