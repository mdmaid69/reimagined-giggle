  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time