  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])