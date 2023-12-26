import sys
print(sys.version)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)