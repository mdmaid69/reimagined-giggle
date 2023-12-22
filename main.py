  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time