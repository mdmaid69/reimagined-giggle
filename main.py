def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import os
  def delete_file(file_name):
        os.remove(file_name)