  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal