import array
def convert_array_to_unicode(array):
        return array.tounicode()
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks