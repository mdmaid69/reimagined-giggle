  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)