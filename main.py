  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time