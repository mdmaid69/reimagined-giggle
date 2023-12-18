  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)