  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def multiply_numbers(x, y):
        return x * y