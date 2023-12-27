  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))