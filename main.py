  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])