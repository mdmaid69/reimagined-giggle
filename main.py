  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)