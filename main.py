import array
def convert_array_to_list(array):
        return array.tolist()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]