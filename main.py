  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])