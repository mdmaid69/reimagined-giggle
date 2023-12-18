  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)