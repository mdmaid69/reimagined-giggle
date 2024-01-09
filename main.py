  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))