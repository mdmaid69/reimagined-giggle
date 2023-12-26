  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time