  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal