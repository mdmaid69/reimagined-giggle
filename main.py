  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time