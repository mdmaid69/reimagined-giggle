  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
def calculate_work(force, distance):
        return force * distance