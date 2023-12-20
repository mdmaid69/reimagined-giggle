  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue