def greet(name):
        print(f"Hello, {name}!")
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid