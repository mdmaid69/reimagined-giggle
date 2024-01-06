  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def cube_number(x):
        return x**3