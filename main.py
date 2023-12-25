  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)