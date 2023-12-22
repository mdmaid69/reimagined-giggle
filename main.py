text = "Hello, world!"
print("Uppercase:", text.upper())
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags