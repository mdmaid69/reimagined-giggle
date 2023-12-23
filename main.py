import array
def get_list_from_array(array):
        return array.tolist()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)