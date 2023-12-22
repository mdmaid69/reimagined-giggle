  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))