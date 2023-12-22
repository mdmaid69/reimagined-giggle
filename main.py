import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)