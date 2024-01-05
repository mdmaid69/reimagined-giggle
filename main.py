def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)