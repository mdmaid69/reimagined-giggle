  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import array
def convert_array_to_unicode(array):
        return array.tounicode()