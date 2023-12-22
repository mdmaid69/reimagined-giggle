n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]