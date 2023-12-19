  import os
  def get_current_working_directory():
        return os.getcwd()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time