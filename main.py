  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))