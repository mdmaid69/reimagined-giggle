  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal