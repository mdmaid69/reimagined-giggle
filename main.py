  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
x = 10
y = 20
print("Sum:", x + y)