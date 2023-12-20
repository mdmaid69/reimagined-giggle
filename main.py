  import os
  def get_current_directory():
        return os.getcwd()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time