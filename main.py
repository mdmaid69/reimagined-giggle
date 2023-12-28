  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
text = "Hello, world!"
print("Uppercase:", text.upper())