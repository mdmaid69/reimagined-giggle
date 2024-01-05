  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time