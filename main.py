  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)