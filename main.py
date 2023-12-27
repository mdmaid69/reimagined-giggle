  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time