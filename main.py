def greet(name):
        print(f"Hello, {name}!")
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns