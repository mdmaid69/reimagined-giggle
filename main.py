  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def convert_array_to_unicode(array):
        return array.tounicode()