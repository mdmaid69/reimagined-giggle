  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))