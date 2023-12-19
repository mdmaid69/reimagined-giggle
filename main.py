def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))