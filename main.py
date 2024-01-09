import array
def get_array_item_count(array, item):
        return array.count(item)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)