def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)