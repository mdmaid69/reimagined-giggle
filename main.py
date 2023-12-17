  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)