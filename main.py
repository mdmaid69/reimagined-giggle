  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])