n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import os
  def get_directory_name(path):
        return os.path.dirname(path)