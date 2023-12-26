def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_current_working_directory():
        return os.getcwd()