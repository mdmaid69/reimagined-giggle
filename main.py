  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
n = 10
print("Cube numbers:", [x**3 for x in range(n)])