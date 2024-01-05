import array
def extend_array(array, iterable):
        array.extend(iterable)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]