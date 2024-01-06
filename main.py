  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_acceleration(speed, time):
        return speed / time