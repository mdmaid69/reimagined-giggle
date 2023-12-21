  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def calculate_work(force, distance):
        return force * distance