  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])