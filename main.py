  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import array
def get_array_item_count(array, item):
        return array.count(item)