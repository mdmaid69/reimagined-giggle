  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)