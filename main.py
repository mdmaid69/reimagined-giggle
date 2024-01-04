  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time