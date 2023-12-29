  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
text = "Hello, world!"
print("Uppercase:", text.upper())