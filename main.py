  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time