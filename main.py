text = "Hello, world!"
print("Reversed:", text[::-1])
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen