  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity