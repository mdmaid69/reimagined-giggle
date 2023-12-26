  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)