  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time