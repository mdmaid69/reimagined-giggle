text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)