  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def calculate_work(force, distance):
        return force * distance