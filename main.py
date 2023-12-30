def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns