def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]