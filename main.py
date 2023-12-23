  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def is_even(n):
        return n % 2 == 0