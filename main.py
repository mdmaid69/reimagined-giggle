import array
def get_string_from_array(array):
        return array.tobytes()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]