import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  def is_even(n):
        return n % 2 == 0