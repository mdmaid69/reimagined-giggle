  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
print([x**2 for x in range(10)])