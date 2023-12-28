def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)