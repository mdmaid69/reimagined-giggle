  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)