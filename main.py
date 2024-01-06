  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import array
def convert_array_to_unicode(array):
        return array.tounicode()