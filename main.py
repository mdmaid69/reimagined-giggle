  import os
  def get_current_directory():
        return os.getcwd()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time