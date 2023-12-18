  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
text = "Hello, world!"
print("Uppercase:", text.upper())