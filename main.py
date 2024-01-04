def calculate_irr(cash_flows):
        rate = 0.1
        for _ in range(100):
        npv = sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
        if abs(npv) < 1e-6:
                return rate
        rate += 0.01
        return None
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))