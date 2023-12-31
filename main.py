  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))