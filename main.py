  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def calculate_area_rectangle(l, w):
        return l * w