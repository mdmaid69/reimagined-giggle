  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def convert_array_to_unicode(array):
        return array.tounicode()