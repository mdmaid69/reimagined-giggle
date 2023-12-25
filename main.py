  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time