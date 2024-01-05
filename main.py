  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time