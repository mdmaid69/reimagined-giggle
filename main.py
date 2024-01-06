def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)