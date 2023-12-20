def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)