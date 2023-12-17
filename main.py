  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def calculate_work(force, distance):
        return force * distance