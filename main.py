  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time