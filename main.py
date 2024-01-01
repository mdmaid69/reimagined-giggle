  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))