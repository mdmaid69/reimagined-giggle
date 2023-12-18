def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)