  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])