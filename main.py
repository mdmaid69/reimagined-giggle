def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]