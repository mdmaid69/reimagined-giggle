import array
def get_list_from_array(array):
        return array.tolist()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)