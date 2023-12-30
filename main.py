  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time