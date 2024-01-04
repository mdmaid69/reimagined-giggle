  import os
  def delete_file(file_name):
        os.remove(file_name)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)