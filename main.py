  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)