  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
text = "Hello, world!"
print("Words:", len(text.split()))