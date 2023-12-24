n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]