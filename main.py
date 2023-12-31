  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import array
def convert_array_to_unicode(array):
        return array.tounicode()