def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)