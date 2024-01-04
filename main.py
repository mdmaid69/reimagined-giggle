  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))