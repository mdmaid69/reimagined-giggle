n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)