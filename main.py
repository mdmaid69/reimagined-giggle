  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import array
def convert_array_to_bytes(array):
        return array.tobytes()