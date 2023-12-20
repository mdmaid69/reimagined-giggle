  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])