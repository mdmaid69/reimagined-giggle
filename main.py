  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def convert_array_to_string(array):
        return array.tostring()