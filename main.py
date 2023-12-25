text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)