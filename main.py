  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def square_number(x):
        return x**2