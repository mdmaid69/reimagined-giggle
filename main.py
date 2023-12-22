def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)