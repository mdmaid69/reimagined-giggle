  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_work(force, distance):
        return force * distance