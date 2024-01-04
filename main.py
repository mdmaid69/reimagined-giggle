import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]