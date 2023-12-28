def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)